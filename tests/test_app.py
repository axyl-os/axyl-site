from axyl_site import create_app


def test_index():
    app = create_app()
    tester = app.test_client()
    response = tester.get("/", content_type="html/text")

    assert response.status_code == 200
    assert "Welcome to Axyl" in str(response.data)