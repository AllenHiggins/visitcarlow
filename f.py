from flask import Flask, jsonify, request
#from flask_cors import CORS
import app_request
import os, uuid


APP_ROOT = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
#CORS(app, resources={r"/*": {"origins": "*"}})



############################################################################
#                                   GET
############################################################################


# get all list types
@app.route('/types/all')
def get_all_types():
    return jsonify({'types': app_request.get_types()}), 202

# get a list of all counties
@app.route('/counties')
def get_county():
    return jsonify({'County': app_request.get_counties()}), 202


# get all categories
@app.route('/category', methods=['GET'])
def cats():
    return jsonify({'Catagories': app_request.get_cats()}), 202


# get all sub categories card data for a category
@app.route("/category/subList/<string:title>", methods=['GET'])
def sub_cat_title_id(title):
    return jsonify({'Subcategories': app_request.sub_title_id(title)})


# get all sub category titles and id's for a category
@app.route("/category/<string:title>", methods=['GET'])
def sub_categories(title):
    return jsonify({'Subcategories': app_request.get_sub_categories(title)})


# get list name, address, county, id for admin editing
@app.route('/listing/admin/display', methods=['GET'])
def get_listing_admin_edit_info():
    return jsonify({'listings': app_request.get_List_Edit_info()}), 200


# get (single) listing data requested by the user
@app.route('/listing/choice/<int:list_id>', methods=['GET'])
def sublist_listings(list_id):
    return jsonify({'Listing': app_request.get_listing(str(list_id))}), 202


@app.route('/listing/image/<int:list_id>', methods=['GET'])
def listing_image(list_id):
    return app_request.get_listing_image(str(list_id)), 202


# get (multiple) listing data for card display by type and county
@app.route('/listings/cards/<string:county>/<string:title>', methods=['GET'])
def cards(title, county):
    return jsonify({title: app_request.get_card_data(title, county)}), 202


#get all (multiple) listings information by county, category and type
@app.route('/listings/search/<string:county>/<string:category>/<string:list_type>', methods=['GET'])
def type_by_county_cat_type(county, category, list_type):
    return jsonify({'Listings': app_request.get_all_type_by_county_category(county, category, list_type)}), 202


# get comment and user name for a listing
@app.route('/listings/comments/request/<int:listing_id>', methods=['GET'])
def get_comments(listing_id):
    return jsonify({'Comments': app_request.get_all_comments_for_listing(str(listing_id))}), 202





############################################################################################################


# get average rating for a listing - calc all ? (should return one overall rating)
@app.route('/listings/rating/request/<int:listing_id>', methods=['GET'])
def get_rating(listing_id):
    return jsonify({'Comments': app_request.get_rating_listing(str(listing_id))}), 202

############################################################################################################






# gets all media links for a listing
@app.route('/listings/media/<int:listing_id>', methods=['GET'])
def get_media_links(listing_id):
    return jsonify({'Media': app_request.get_medialinks_for_listing(str(listing_id))}), 202


# gets users favorites list
@app.route('/user/favorites/<int:user_id>', methods=['GET'])
def user_favorites(user_id):
    return jsonify({'Favorites': app_request.get_favorites_for_user(str(user_id))}), 202


# gets the view count of a listing - ie how many times it was viewed
@app.route('/listing/view/count/<int:list_id>', methods=['GET'])
def get_view_count_for_listing(list_id):
    return jsonify({'result': app_request.view_count(str(list_id))}), 202


# gets all id of nearby listings for a listing
@app.route('/listing/related/<int:list_id>', methods=['GET'])
def get_nearby_listing_ids(list_id):
    return jsonify({'result': app_request.get_nearby_listings(str(list_id))}), 202


############################################################################
#                                   POST
############################################################################


# All image uploads should use this single endpoint
# upload a image for a listing with listing name and id
@app.route('/image/upload/<id>', methods=['POST'])
def upload_image(id):

    ######## NEED TO CHECK FILE TYPE! ###########

    folder = 'images\\' + str(uuid.uuid4())
    target = os.path.join(APP_ROOT, folder)

    if not os.path.isdir(target):
        os.mkdir(target)

    path = ''
    for file in request.files.getlist("image"):
        file_name = file.filename
        path = '\\'.join([target, file_name])
        file.save(path)

    result = app_request.add_image_to_DB(str(path),str('listing'),str(id))
    return jsonify({'result':result, 'path': path})


# add a new listing to the list of listings
@app.route('/listing/add', methods=['POST'])
def create_new_listing():
    try:
        data = {
            'list_type_id': request.json['typeID'],
            'county_id': request.json['countID'],
            'name': request.json['name'],
            'address': request.json['address'],
            'latitude': request.json['latitude'],
            'longitude': request.json['longitude'],
            'text': request.json['text'],
            'phone': request.json['phone'],
            'email': request.json['email'],
            'website': request.json['website'],
            'facebook': request.json['facebook'],
            'twitter': request.json['twitter'],
            'instagram': request.json['instagram'],
        }
    except:
        return jsonify({'expecting': {
            'typeID': 'int',
            'countID': 'int',
            'name': 'string',
            'address': 'string',
            'latitude': 'string',
            'longitude': 'string',
            'text': 'string',
            'phone': 'string',
            'email': 'string',
            'website': 'string',
            'facebook': 'string',
            'twitter': 'string',
            'instagram': 'string',
        }}), 404
    return jsonify({'result': app_request.create_listing(data)}), 202


# add or update a users rating to a listing
@app.route('/listing/ratings/add', methods=['POST'])
def add_user_rating():
    try:
        data = {
            'list_id': request.json['listID'],
            'user_id': request.json['userID'],
            'rating': request.json['rating']
        }
    except:
        return jsonify({'expecting': {
            'listID': 'int',
            'userID': 'int',
            'rating': 'int'
        }}), 404
    return jsonify({'result': app_request.create_rating(data)}), 202


# add or update a users comment to a listing
@app.route('/listing/comments/add', methods=['POST'])
def add_user_comment():
    try:
        data = {
            'list_id': request.json['listID'],
            'user_id': request.json['userID'],
            'comment': request.json['comment']
        }
    except:
        return jsonify({'expecting': {
            'listID': 'int',
            'userID': 'int',
            'comment': 'string'
        }}), 404
    return jsonify({'result': app_request.create_comment(data)}), 202


# adds a listing to the users favorites list - take JSON from client
@app.route('/user/favorites/add', methods=['POST'])
def add_to_favorites():
    try:
        data = {
            'list_id': request.json['list_id'],
            'user_id': request.json['user_id']
        }
    except:
        return jsonify({'expecting': {
            'list_id': 'int',
            'user_id': 'int',
        }}), 404
    return jsonify({'result': app_request.add_listing_to_users_favorites(data)}), 202


# removes a listing from the users favorites list - take JSON from client
@app.route('/user/favorites/remove', methods=['POST'])
def remove_from_favorites():
    try:
        data = {
            'list_id': request.json['list_id'],
            'user_id': request.json['user_id']
        }
    except:
        return jsonify({'expecting': {
            'list_id': 'int',
            'user_id': 'int',
        }}), 404
    return jsonify({'result': app_request.remove_listing_to_users_favorites(data)}), 202


# report a comment
@app.route('/listing/comment/report', methods=['POST'])
def report_a_comment():
    try:
        data = {'commentID':  request.json['commentID']}
    except:
        return jsonify({'expecting': {'commentID': 'int'}}), 404
    return jsonify({'result': app_request.report_comment(data)}), 202


# update a single listing
@app.route('/listing/details/edit', methods=['POST'])
def update_listing_details():
    try:
        data = {
            'id': request.json['id'],
            'name': request.json['name'],
            'address': request.json['address'],
            'latitude': request.json['latitude'],
            'longitude': request.json['longitude'],
            'text': request.json['text'],
            'phone': request.json['phone'],
            'email': request.json['email'],
            'listTypeID': request.json['listTypeID'],
            'countyID': request.json['countyID'],
            'website': request.json['website'],
            'facebook': request.json['facebook'],
            'twitter': request.json['twitter'],
            'instagram': request.json['instagram']
        }
    except:
        return jsonify({'expecting': {
            'id': 'int',
            'name': 'string',
            'address': 'string',
            'latitude': 'string',
            'longitude': 'string',
            'text': 'string',
            'phone': 'string',
            'email': 'string',
            'listTypeID': 'int',
            'countyID': 'int',
            'website':'string',
            'facebook': 'string',
            'twitter': 'string',
            'instagram': 'string'
        }}), 404
    return jsonify({'result': app_request.update_listing(data)}), 202


############################################################################
#                                BAD REQUEST
############################################################################

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Bad Request'}), 404


@app.errorhandler(405)
def not_found(error):
    return jsonify({'error': 'Bad Request'}), 405


if __name__ == '__main__':
    app.run(debug=True)
