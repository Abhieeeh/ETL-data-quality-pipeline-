import os
import subprocess
from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Mount static files folder
static_dir = os.path.join(BASE_DIR, 'dashboard', 'static')
app.mount("/static", StaticFiles(directory=static_dir), name="static")

def get_empty_data():
    return {
        'customers': {'name': 'Customers', 'total': 0, 'valid': 0, 'invalid': 0, 'error_rate': '0.0%', 'errors': []},
        'orders': {'name': 'Orders', 'total': 0, 'valid': 0, 'invalid': 0, 'error_rate': '0.0%', 'errors': []},
        'support_tickets': {'name': 'Support Tickets', 'total': 0, 'valid': 0, 'invalid': 0, 'error_rate': '0.0%', 'errors': []}
    }

def load_data():
    report_path = os.path.join(BASE_DIR, 'reports', 'data_quality_report.csv')
    if not os.path.exists(report_path):
        return get_empty_data()
    
    try:
        import pandas as pd
        df = pd.read_csv(report_path)
        data = {}
        
        # Standardize expected rows
        for _, row in df.iterrows():
            dataset = row['Dataset'] # 'Orders', 'Customers', 'Support Tickets'
            total = int(row['Total'])
            valid = int(row['Valid'])
            invalid = int(row['Invalid'])
            valid_pct = float(row['Valid %'])
            error_rate = 100.0 - valid_pct
            
            # Map dataset names to filenames
            if dataset == 'Support Tickets':
                err_filename = "Support_ticket_error_details.csv"
            else:
                err_filename = f"{dataset}_error_details.csv"
                
            err_path = os.path.join(BASE_DIR, 'reports', err_filename)
            errors = []
            if os.path.exists(err_path):
                err_df = pd.read_csv(err_path)
                for _, err_row in err_df.iterrows():
                    errors.append({
                        'error': err_row['Error'],
                        'count': int(err_row['count'])
                    })
            
            key = dataset.lower().replace(' ', '_')
            data[key] = {
                'name': dataset,
                'total': total,
                'valid': valid,
                'invalid': invalid,
                'error_rate': f"{error_rate:.1f}%",
                'errors': errors
            }
            
        # Ensure all keys exist
        default_data = get_empty_data()
        for k in default_data:
            if k not in data:
                data[k] = default_data[k]
                
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return get_empty_data()

@app.get('/')
def index():
    template_path = os.path.join(BASE_DIR, 'dashboard', 'templates', 'index.html')
    return FileResponse(template_path)

@app.get('/api/metrics')
def api_metrics():
    return load_data()

@app.post('/api/run-pipeline')
def run_pipeline():
    try:
        main_py = os.path.join(BASE_DIR, 'main.py')
        result = subprocess.run(
            ['python', main_py],
            cwd=BASE_DIR,
            capture_output=True,
            text=True
        )
        
        success = result.returncode == 0
        output = result.stdout + "\n" + result.stderr
        
        log_path = os.path.join(BASE_DIR, 'logs', 'etl_pipeline.log')
        file_logs = ""
        if os.path.exists(log_path):
            with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
                file_logs = "".join(lines[-20:]) # last 20 lines
                
        metrics = load_data()
        
        return {
            'success': success,
            'output': output,
            'file_logs': file_logs,
            'metrics': metrics
        }
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                'success': False,
                'output': str(e),
                'file_logs': '',
                'metrics': get_empty_data()
            }
        )

if __name__ == '__main__':
    import uvicorn
    # Run server locally on port 5000
    uvicorn.run(app, host='127.0.0.1', port=5000)
