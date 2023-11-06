# importing the packagaes
from flask import Flask

# create an instance of the flask application
app = Flask(__name__)

# homepage - app route
@app.route('/')
def index():
    return 'Welcome to Crew Scheduling App!'

# second page - # assume module one page
@app.route('/optimize')
def optimize_crew_schedule():
    # Call your optimization function here
    # Example:
    # result = solve_routing_problem()
    return 'Optimization completed'  # Return the result

# initialize the application
if __name__ == '__main__':
    app.run(debug=True)