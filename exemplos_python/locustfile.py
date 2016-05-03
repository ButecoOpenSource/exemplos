from locust import HttpLocust, TaskSet, task

class WebsiteTasks(TaskSet):
    def on_start(self):
        self.client.post("/login", {
            "username": "test_user",
            "password": ""
        })
    
    @task
    def index(self):
        self.client.get("/")
        
    @task
    def about(self):
        self.client.get("/about/")

    @task
    def catch_response(self):
        with self.client.get('/pagina-teste', catch_response=True) as r:
            if r.status_code == 404:
                r.success()
            else:
                r.failure('A página não deveria existir.')

class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    min_wait = 5000
    max_wait = 15000
