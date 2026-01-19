# Source: Row 28 in ./dataset/CVEfixes/Analysis/results/Python/df_python_cwe_352.xlsx

def test_get_delete_dataobj(test_app, client: FlaskClient, note_fixture):
    response = client.post("/dataobj/delete/1")
    assert response.status_code == 302