let currentMetrics = {};
let activeTab = 'customers'; // default

// Helper to format numbers with commas
function formatNum(val) {
    if (val === undefined || val === null) return '0';
    return Number(val).toLocaleString();
}

async function fetchMetrics() {
    try {
        const response = await fetch('/api/metrics');
        if (!response.ok) throw new Error('Failed to fetch metrics');
        currentMetrics = await response.json();
        updateUI();
    } catch (err) {
        console.error('Error fetching metrics:', err);
    }
}

function updateUI() {
    // Update total values in tab buttons
    if (currentMetrics.customers) {
        document.getElementById('val-customers-total').innerText = formatNum(currentMetrics.customers.total);
    }
    if (currentMetrics.orders) {
        document.getElementById('val-orders-total').innerText = formatNum(currentMetrics.orders.total);
    }
    if (currentMetrics.support_tickets) {
        document.getElementById('val-tickets-total').innerText = formatNum(currentMetrics.support_tickets.total);
    }

    // Refresh display of the active tab
    renderActiveTabDetails();
}

function renderActiveTabDetails() {
    const data = currentMetrics[activeTab];
    if (!data) return;

    // Update tab active styling
    const tabs = ['customers', 'orders', 'support_tickets'];
    tabs.forEach(t => {
        const btn = document.getElementById(`tab-${t}`);
        if (t === activeTab) {
            btn.classList.add('active');
        } else {
            btn.classList.remove('active');
        }
    });

    // Update main metrics section
    document.getElementById('val-valid').innerText = formatNum(data.valid);
    document.getElementById('val-invalid').innerText = formatNum(data.invalid);
    document.getElementById('val-error-rate').innerText = data.error_rate;

    // Update errors section
    const container = document.getElementById('error-list-container');
    container.innerHTML = ''; // clear

    if (data.errors && data.errors.length > 0) {
        data.errors.forEach(err => {
            const item = document.createElement('div');
            item.className = 'error-item';
            
            const nameSpan = document.createElement('span');
            nameSpan.className = 'error-name';
            nameSpan.innerText = err.error;

            const countSpan = document.createElement('span');
            countSpan.className = 'error-count';
            countSpan.innerText = formatNum(err.count);

            item.appendChild(nameSpan);
            item.appendChild(countSpan);
            container.appendChild(item);
        });
    } else {
        const emptyState = document.createElement('div');
        emptyState.className = 'error-item empty-state';
        emptyState.innerText = 'No validation errors found.';
        container.appendChild(emptyState);
    }
}

function switchTab(tabKey) {
    activeTab = tabKey;
    renderActiveTabDetails();
}

async function runPipeline() {
    const runBtn = document.getElementById('run-btn');
    const logContainer = document.getElementById('log-container');
    const logOutput = document.getElementById('log-output');

    // UI Feedback for running
    runBtn.disabled = true;
    runBtn.innerText = '[ Running Pipeline... ]';
    logContainer.style.display = 'flex';
    logOutput.innerText = 'Executing main.py in the background...\nLoading raw CSV files...\nApplying transformations...\nValidating records...\nGenerating data quality reports...';

    try {
        const response = await fetch('/api/run-pipeline', {
            method: 'POST'
        });
        const result = await response.json();

        if (result.success) {
            logOutput.innerText = `Pipeline completed successfully!\n\nConsole logs:\n${result.output}\n\nFile logs:\n${result.file_logs}`;
        } else {
            logOutput.innerText = `Pipeline failed!\n\nError output:\n${result.output}`;
        }

        // Update metrics with the response
        if (result.metrics) {
            currentMetrics = result.metrics;
            updateUI();
        }

    } catch (err) {
        logOutput.innerText = `Error contacting server to run pipeline: ${err.message}`;
    } finally {
        runBtn.disabled = false;
        runBtn.innerText = '[ Run ETL Pipeline ]';
    }
}

function closeLogs() {
    document.getElementById('log-container').style.display = 'none';
}

// Initial load
window.addEventListener('DOMContentLoaded', fetchMetrics);
