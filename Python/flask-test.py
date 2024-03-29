
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask

def sensor():
    """ Function for test purposes. """
    print("Scheduler is alive!")

sched = BackgroundScheduler(daemon=True)
sched.add_job(sensor,'interval',seconds=5)
sched.start()


app = Flask(__name__)

@app.route("/")
def home():
    return "test"

if __name__ == "__main__":
    app.run()