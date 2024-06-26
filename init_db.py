from app import create_app, db

# Create the Flask app
app = create_app()

# Use the application context
with app.app_context():
    # Create the database tables
    db.create_all()
