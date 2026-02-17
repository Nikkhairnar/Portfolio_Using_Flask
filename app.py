from flask import Flask, render_template

app = Flask(__name__)

PERSONAL_INFO = {
    'name': 'Nik Khairnar',
    'title': 'Web Developer',
    'bio': 'Developer focused on building simple, reliable web experiences with Python and Flask.',
    'email': 'nhkhairnar11122004@gmail.com',
    'github': 'https://github.com/Nikkhairnar',
    'linkedin': 'www.linkedin.com/in/nikhil-khairnar-b34163326',
}

SKILLS = [
    {'name': 'Python', 'level': 90},
    {'name': 'Cloud', 'level': 85},
    {'name': 'HTML', 'level': 80},
    {'name': 'C++', 'level': 70},
    {'name': 'SQL', 'level': 65},
]

PROJECTS = [
    {'id': 1, 'name': 'Personal Portfolio', 'description': 'A responsive portfolio built with Flask showcasing projects, skills, and contact info.', 'tech': ['Python', 'Flask', 'HTML', 'CSS'], 'status': 'In Progress'},
    {'id': 2, 'name': 'Python Quiz App', 'description': 'A command-line quiz app built using python with user score tracking and dynamic questions', 'tech': ['Python'], 'status': 'Completed'},
    {'id': 3, 'name': 'Weather Dashboard', 'description': 'Dashboard that consumes a public weather API and visualizes forecasts.', 'tech': ['Python', 'Flask', 'API', 'JavaScript'], 'status': 'Planned'},
]

BLOG_POSTS = [
    {
        'id': 1,
        'title': 'Getting Started with Flask',
        'summary': 'A quick overview of setting up a minimal Flask app and structuring routes.',
        'content': 'Flask makes it easy to start small and grow. Begin by creating an app instance, define a few routes, and use templates to render HTML. As the project grows, split code into blueprints and keep your templates organized.',
        'tags': ['Flask', 'Python', 'Getting Started'],
    },
    {
        'id': 2,
        'title': 'Designing Clean APIs',
        'summary': 'Thoughts on planning endpoints, choosing verbs, and keeping responses consistent.',
        'content': 'Start with the client in mind: name endpoints around resources, use clear HTTP verbs, and return consistent JSON structures. Add validation early and document common error shapes so consumers know what to expect.',
        'tags': ['API', 'Design', 'Best Practices'],
    },
    {
        'id': 3,
        'title': 'Building Side Projects That Ship',
        'summary': 'Practical tips to scope, prioritize, and deploy small ideas without getting stuck.',
        'content': 'Pick a tiny scope, ship a first version fast, and collect feedback. Automate deploys with simple scripts, add logging, and iterate weekly. Momentum comes from finishing small slices instead of waiting for perfect features.',
        'tags': ['Productivity', 'Projects', 'Deployment'],
    },
]


# =============================================================================
# ROUTES
# =============================================================================

@app.route('/')
def home():
    return render_template('index.html', info=PERSONAL_INFO)


@app.route('/about')
def about():
    return render_template('about.html', info=PERSONAL_INFO, skills=SKILLS)


@app.route('/projects')
def projects():
    return render_template('projects.html', info=PERSONAL_INFO, projects=PROJECTS)


@app.route('/project/<int:project_id>')  # Dynamic route for individual project
def project_detail(project_id):
    project = None
    for p in PROJECTS:
        if p['id'] == project_id:
            project = p
            break
    return render_template('project_detail.html', info=PERSONAL_INFO, project=project, project_id=project_id)


@app.route('/blog')
def blog():
    return render_template('blog.html', info=PERSONAL_INFO, posts=BLOG_POSTS)


@app.route('/blog/<int:post_id>')
def blog_detail(post_id):
    post = None
    for p in BLOG_POSTS:
        if p['id'] == post_id:
            post = p
            break
    return render_template('blog_detail.html', info=PERSONAL_INFO, post=post, post_id=post_id)


@app.route('/skill/<skill_name>')
def skill(skill_name):
    matching_projects = []
    for project in PROJECTS:
        tech_stack = [tech.lower() for tech in project['tech']]
        if skill_name.lower() in tech_stack:
            matching_projects.append(project)
    return render_template('skill.html', info=PERSONAL_INFO, skill_name=skill_name, projects=matching_projects)


@app.route('/contact')
def contact():
    return render_template('contact.html', info=PERSONAL_INFO)


if __name__ == '__main__':
    app.run(debug=True)


# =============================================================================
# PROJECT STRUCTURE:
# =============================================================================
#
# part-5/
# ├── app.py              <- You are here
# ├── static/
# │   └── style.css       <- CSS styles
# └── templates/
#     ├── base.html       <- Base template (inherited by all pages)
#     ├── index.html      <- Home page
#     ├── about.html      <- About page
#     ├── projects.html   <- Projects list
#     ├── project_detail.html <- Single project view
#     └── contact.html    <- Contact page
#
# =============================================================================

