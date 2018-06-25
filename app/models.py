# -*- coding: UTF-8 -*-
from flask_sqlalchemy import SQLAlchemy
from app.extensions import bcrypt
from flask_login import AnonymousUserMixin

# Init the sqlalchemy object
db = SQLAlchemy()

users_roles = db.Table('users_roles',
    db.Column('user_id', db.String(45), db.ForeignKey('users.id')),
    db.Column('role_id', db.String(45), db.ForeignKey('roles.id')))


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(45), primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    posts = db.relationship(
        'Post',
        backref='users',
        lazy='dynamic'
    )

    roles = db.relationship(
        'Role',
        secondary=users_roles,
        backref=db.backref('users', lazy='dynamic'))

    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = self.set_password(password)

        # Setup the default-role for user
        default = Role.query.filter_by(name="default").one()
        self.roles.append(default)

    def __repr__(self):
        return "<Model User `{}`>".format(self.username)

    def set_password(self, password):
        """Convert the password to cryptograph via flask-bcrypt"""
        return bcrypt.generate_password_hash(password)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    def is_authenticated(self):
        """Check the user whether logged in."""

        # Check the User's instance whether Class AnonymousUserMixin's instance.
        if isinstance(self, AnonymousUserMixin):
            return False
        else:
            return True

    def is_active(self):
        """Check the user whether pass the activation process."""

        return True

    def is_anonymous(self):
        """Check the user's login status whether is anonymous."""

        if isinstance(self, AnonymousUserMixin):
            return True
        else:
            return False

    def get_id(self):
        """Get the user's uuid from database."""

        return self.id


class Role(db.Model):
    """Represents Proected roles."""
    __tablename__ = 'roles'

    id = db.Column(db.String(45), primary_key=True)
    name = db.Column(db.String(255), unique=True)
    description = db.Column(db.String(255))

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return "<Model Role `{}`>".format(self.name)


posts_tags = db.Table('posts_tags',
                      db.Column('post_id', db.String(45), db.ForeignKey('posts.id')),
                      db.Column('tag_id', db.String(45), db.ForeignKey('tags.id')))


class Post(db.Model):
    """ Represents Proected posts. """

    __tablename__ = 'posts'
    id = db.Column(db.String(45), primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.Text())
    publish_date = db.Column(db.DateTime)
    # set the foreign key for Post
    user_id = db.Column(db.String(45), db.ForeignKey('users.id'))
    # establish contact with Comment's ForeignKey: post_id
    comments = db.relationship(
        'Comment',
        backref='posts',
        lazy='dynamic'
    )
    # many to many: posts<=>tags
    tags = db.relationship(
        'Tag',
        secondary=posts_tags,
        backref=db.backref('posts', lazy='dynamic')
    )

    def __init__(self, id, title):
        self.id = id
        self.title = title

    def __repr__(self):
        return "<Model Post `{}`>".format(self.title)


class Comment(db.Model):
    """ Represents Proected comments. """

    __tablename__ = 'comments'
    id = db.Column(db.String(45), primary_key=True)
    name = db.Column(db.String(255))
    text = db.Column(db.Text())
    date = db.Column(db.DateTime)
    post_id = db.Column(db.String(45), db.ForeignKey('posts.id'))

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return "<Model Comment `{}`>".format(self.name)


class Tag(db.Model):
    """ Represents Proected tags. """

    __tablename__ = 'tags'
    id = db.Column(db.String(45), primary_key=True)
    name = db.Column(db.String(255))

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return "<Model Tag `{}`>".format(self.name)
