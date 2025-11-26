from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = 'dev-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# -------------------------
# Database Model
# -------------------------
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Post {self.id} - {self.title}>"


# -------------------------
# Blog Routes
# -------------------------

# Home / All posts
@app.route('/')
def index():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template('index.html', posts=posts)

# Single post
@app.route('/post/<int:post_id>')
def post_detail(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post_detail.html', post=post)

# Create post
@app.route('/create', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')

        if not title or not content:
            flash("Title and content are required.", "error")
            return redirect(url_for('create_post'))

        new_post = Post(title=title, content=content)
        db.session.add(new_post)
        db.session.commit()
        flash("Post created successfully!", "success")
        return redirect(url_for('index'))

    return render_template('create_post.html')

# Edit post
@app.route('/edit/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)

    if request.method == 'POST':
        post.title = request.form.get('title')
        post.content = request.form.get('content')

        if not post.title or not post.content:
            flash("Title and content are required.", "error")
            return redirect(url_for('edit_post', post_id=post.id))

        db.session.commit()
        flash("Post updated successfully!", "success")
        return redirect(url_for('post_detail', post_id=post.id))

    return render_template('edit_post.html', post=post)

# Delete post
@app.route('/delete/<int:post_id>', methods=['POST'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash("Post deleted successfully!", "success")
    return redirect(url_for('index'))


# -------------------------
# Portfolio / Extra Pages
# -------------------------

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/projects')
def projects():
    # You can later replace this with DB or more complex data
    projects_data = [
        {
            "title": "HIV Dataset Analytics & SQL Automation",
            "desc": "Explored global HIV data with SQL, triggers, and stored procedures to automate reporting.",
            "tags": ["SQL", "Oracle", "Data Analytics"]
        },
        {
            "title": "Stock Price Prediction Pipeline",
            "desc": "Built an end-to-end ML pipeline using Python, Snowflake, and Airflow to forecast stock prices.",
            "tags": ["Python", "Snowflake", "Airflow", "ML"]
        },
        {
            "title": "Healthcare RPA Automation",
            "desc": "Automated eligibility verification & invoice posting to save 5,600+ hours annually.",
            "tags": ["UiPath", "RPA", "Healthcare"]
        },
    ]
    return render_template('projects.html', projects=projects_data)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name', '')
        email = request.form.get('email', '')
        message = request.form.get('message', '')

        # For now, just flash the message instead of sending email
        if not name or not email or not message:
            flash("Please fill out all contact fields.", "error")
        else:
            flash("Thank you for reaching out, your message has been received! 💌", "success")

        return redirect(url_for('contact'))

    return render_template('contact.html')


# -------------------------
# App Entry
# -------------------------
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
