import pandas as pd
import pytest

from validate.validate_support_ticket import validate_support_ticket

def test_validate_support_ticket():
    df=pd.DataFrame({
        "ticket_id":["101"],
        "customer_id":["201"],
        "issue_type":["xyz"],
        "ticket_created":["28/2/2026"],
        "ticket_resolved":["28/8/2026"],
        "support_agent":["abc"],
        "sentiment":["neutral"],
        "resolution_time_hours":[200]     
    })
    valid,invalid=validate_support_ticket(df)
    assert len(valid)==1
    assert len(invalid)==0


def test_invalid_time():
    df=pd.DataFrame({
        "ticket_id":["101"],
        "customer_id":["201"],
        "issue_type":["xyz"],
        "ticket_created":["28/2/2026"],
        "ticket_resolved":["28/8/2026"],
        "support_agent":["abc"],
        "sentiment":["neutral"],
        "resolution_time_hours":[-200]     
    })
    valid,invalid=validate_support_ticket(df)
    assert len(valid)==0
    assert len(invalid)==1

def test_ticket_id():
    df=pd.DataFrame({
        "ticket_id":[None],
        "customer_id":["201"],
        "issue_type":["xyz"],
        "ticket_created":["28/2/2026"],
        "ticket_resolved":["28/8/2026"],
        "support_agent":["abc"],
        "sentiment":["neutral"],
        "resolution_time_hours":[200]     
    })
    valid,invalid=validate_support_ticket(df)
    assert len(valid)==0
    assert len(invalid)==1

def test_issue_type():
    df=pd.DataFrame({
        "ticket_id":["101"],
        "customer_id":["201"],
        "issue_type":[None],
        "ticket_created":["28/2/2026"],
        "ticket_resolved":["28/8/2026"],
        "support_agent":["abc"],
        "sentiment":["neutral"],
        "resolution_time_hours":[200]     
    })
    valid,invalid=validate_support_ticket(df)
    assert len(valid)==0
    assert len(invalid)==1

def test_support_agent():
    df=pd.DataFrame({
        "ticket_id":["101"],
        "customer_id":["201"],
        "issue_type":["xyz"],
        "ticket_created":["28/2/2026"],
        "ticket_resolved":["28/8/2026"],
        "support_agent":[None],
        "sentiment":["neutral"],
        "resolution_time_hours":[200]     
    })
    valid,invalid=validate_support_ticket(df)
    assert len(valid)==0
    assert len(invalid)==1


def test_sentiment():
    df=pd.DataFrame({
        "ticket_id":["101"],
        "customer_id":["201"],
        "issue_type":["xyz"],
        "ticket_created":["28/2/2026"],
        "ticket_resolved":["28/8/2026"],
        "support_agent":["abc"],
        "sentiment":[None],
        "resolution_time_hours":[200]     
    })
    valid,invalid=validate_support_ticket(df)
    assert len(valid)==0
    assert len(invalid)==1