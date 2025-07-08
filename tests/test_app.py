from app import app

def test_home():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert "Chào mừng" in response.data.decode('utf-8')
