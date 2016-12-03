# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------
import datetime


def get_user_name_from_email(email):
    """Returns a string corresponding to the user first and last names,
    given the user email."""
    u = db(db.auth_user.email == email).select().first()
    if u is None:
        return 'None'
    else:
        return ' '.join([u.first_name, u.last_name])



def index():
    """
    This is your main controller.
    """

    # # Test
    # db.post.truncate()
    # db.post.insert(post_title="DUMMY TITLE1", post_content="dummy content!", user_email="Default Author")
    # db.post.insert(post_title="DUMMY TITLE2", post_content="dummy content!", user_email="Default Author")
    # db.post.insert(post_title="DUMMY TITLE3", post_content="dummy content!", user_email="Default Author")
    # db.post.insert(post_title="DUMMY TITLE4", post_content="dummy content!", user_email="Default Author")
    # db.post.insert(post_title="DUMMY TITLE5", post_content="dummy  content!", user_email="Default Author")
    # db.post.insert(post_title="DUMMY TITLE6", post_content="dummy content!", user_email="Default Author")
    # db.post.insert(post_title="DUMMY TITLE7", post_content="dummy content!", user_email="Default Author")
    # db.post.insert(post_title="DUMMY TITLE8", post_content="dummy content!", user_email="Default Author")
    # db.post.insert(post_title="DUMMY TITLE9", post_content="dummy content!", user_email="Default Author")
    # db.post.insert(post_title="DUMMY TITLE10", post_content="dummy content!", user_email="Default Author")
    #
    subjects = ["All Subjects", "Academic English", "American Studies", "Anthropology", "Applied Linguistics",
                "Applied Math and Statistics", "Arabic", "Art", "Art&Des:Games&PlayableMedia",
                "Astronomy and Astrophysics",
                "Biochemistry and Molecular Bio", "Biology: Molecular Cell & Dev", "Biology: Molecular Cell & Dev",
                "Biology: Ecology & Evolutionary", "Biomolecular Engineering", "Carson College",
                "Chemistry and Biochemistry", "Chinese", "College Eight", "College Nine", "College Ten",
                "Community Studies", "Computational Media", "Computer Engineering", "Computer Science",
                "Cowell College",
                "Creative Writing", "Critical Race & Ethnic Studies", "Crown College", "Digital Arts and New Media",
                "Earth Sciences", "Economics", "Education", "Electrical Engineering", "Engineering",
                "English-Language Literatures", "Environmental Studies", "Environmental Toxicology", "Feminist Studies",
                "Film and Digital Media", "French", "French Literature", "Games and Playable Media", "German",
                "German Literate", "Greek", "Greek Literature", "Hebrew", "Hindi", "History",
                "History of Art&Visual Culture", "History of Consciousness", "Humanities",
                "Information systems management",
                "Italian", "Italian Literature", "Japanese", "Jewish Studies", "Kresge College", "Languages", "Latin",
                "Latin American&Latino Studies", "Latin Literature", "Legal Studies", "Linguistics", "Literature",
                "Mathematics", "Merrill College", "Microbiol & Environ Toxicology", "Modern Literary Studies", "Music",
                "Oakes College", "Ocean Sciences", "Philosophy", "Physical Education", "Physics", "Politics",
                "Porter College", "Portuguese", "Pre & Early Modern Literature", "Psychology", "Punjabi", "Russian",
                "Science Communication", "Social Documentation", "Social Sciences", "Sociology", "Spanish",
                "Spanish for Heritage Speakers", "Spanish for Spanish Speakers", "Spanish/Latin Amer/Latino Lit",
                "Stevenson College", "Technology & Info Management", "Theater Arts", "UCDC", "Women's Studies",
                "World Lit & Cultural Studies", "Writing", "Yiddish"]

    return dict(subjects=subjects)


@auth.requires_login()
def edit():
    """
    This is the page to create / edit / delete a post.
    """
    return dict()


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()



