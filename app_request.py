import pymysql


# connection to database
def connect():
    conn = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='4myself',
        database='visitcarlow')
    return conn


##############################################################
#                        HELPER FUNCTIONS
##############################################################

# get all data for categories and sub categories - helper function
def pares_cat_and_sub_data(data):
    d = []
    for listing in data:
        d.append({'id': listing[0], 'title': listing[1], 'image': listing[2]})
    return d


# get all sub categories for card data display - helper function
def pares_sublisting_card_data(data):
    d = []
    for listing in data:
        d.append({'id': listing[0],
                  'image': listing[1],
                  'name': listing[2],
                  'latitude': listing[3],
                  'longitude': listing[4]})
    return d


##############################################################
#                           GET
##############################################################

# get all linting types
def get_types():
    conn = connect()
    a = conn.cursor()
    try:
        _SQL = "select * from listtype where active = 1;"
        a.execute(_SQL)
        data = a.fetchall()
        data = pares_cat_and_sub_data(data)
    except:
        data = 'fail'
    a.close()
    return data

# return a list of all counties
def get_counties():
    conn = connect()
    a = conn.cursor()
    try:
        _SQL = "select * from county where active = 1;"
        a.execute(_SQL)
        data = a.fetchall()
        data = pares_cat_and_sub_data(data)
    except:
        data = 'fail'
    a.close()
    return data

# get all categories
def get_cats():
    conn = connect()
    a = conn.cursor()
    try:
        _SQL = "select * from catagories where active = 1;"
        a.execute(_SQL)
        data = a.fetchall()
        data = pares_cat_and_sub_data(data)
    except:
        data = 'fail'
    a.close()
    return data


# get all sub categories card data for a selected category
# takes sub_title id as argument in URL
def sub_title_id(title):
    conn = connect()
    a = conn.cursor()
    # avoid sql injection
    title = conn.escape_string(str(title))
    try:
        # check if sub type is in listtype table
        _SQL = ('SELECT id  from catagories WHERE title = "' + title + '"')
        result = a.execute(_SQL)
        # if the row was found
        if result is not 0:
            _SQL = "select listtype.id,listtype.title from listtype\
                   inner join catagories on listtype.catID = catagories.id where catagories.title = '" + title + "' and listtype.active = 1"
            a.execute(_SQL)
            data = a.fetchall()
            d = []
            for listing in data:
                d.append({'id': listing[0], 'title': listing[1]})
            data = d
        else:
            data = 'title not found'
    except:
        data = 'fail'
    a.close()
    return data


# get all sub categories card data for a selected category
# takes title id as argument in URL
def get_sub_categories(title):
    conn = connect()
    a = conn.cursor()
    # avoid sql injection
    title = conn.escape_string(str(title))
    try:
        # check if sub type is in listtype table
        _SQL = ('SELECT id  from catagories WHERE title = "' + title + '"')
        result = a.execute(_SQL)
        # if the row was found
        if result is not 0:
            _SQL = "select listtype.id,listtype.title,listtype.image from listtype\
                   inner join catagories on listtype.catID = catagories.id where catagories.title = '" + title + "' and listtype.active = 1"
            a.execute(_SQL)
            data = a.fetchall()
            data = pares_cat_and_sub_data(data)
        else:
            data = 'title not found'
    except:
        data = 'fail'
    a.close()
    return data

##########################################could do inner join with other tables - nearby,media,comments

# view a listing selected by the user and update the view count
# takes list id as argument in URL
def get_listing(list_id):
    conn = connect()
    a = conn.cursor()
    # avoid sql injection
    list_id = conn.escape_string(str(list_id))
    try:
        # check if listing is in listing table
        _SQL = ('SELECT id  from listing WHERE id = "' + list_id + '"')
        result = a.execute(_SQL)
        # if the row was found
        if result is not 0:
            _SQL = "select id,name,address,text,phone,email,latitude,longitude,image,listTypeID,countyID\
             from listing where id = "+ list_id + " and active = 1;"
            a.execute(_SQL)
            data = a.fetchall()
            d = []
            for listing in data:
                d.append({'id': listing[0],
                          'name': listing[1],
                          'address': listing[2],
                          'text': listing[3],
                          'phone': listing[4],
                          'email': listing[5],
                          'latitude': listing[6],
                          'longitude': listing[7],
                          'image': listing[8],
                          'listTypeID': listing[9],
                          'countyID': listing[10]
                })
            a.execute('UPDATE `listing` SET `view_count`= `view_count`+ 1 WHERE id = ' + list_id)
            conn.commit()
            data = d
        else:
            data = 'listing not found'
    except:
        data = 'fail'
        conn.rollback()
    a.close()
    return data


# get a (single) listing image
def get_listing_image(list_id):
    conn = connect()
    a = conn.cursor()
    # avoid sql injection
    list_id = conn.escape_string(str(list_id))
    try:
        # check if listing is in listing table
        _SQL = ('SELECT id  from listing WHERE id = "' + list_id + '"')
        result = a.execute(_SQL)
        # if the row was found
        if result is not 0:
            _SQL = "select image from listing where id = "+ list_id + " and active = 1;"
            a.execute(_SQL)
            conn.commit()
            data = a.fetchall()
            print(data[0][0])
            return data[0][0]
        else:
            return 'listing not found'
    except:
        data = 'fail'
        conn.rollback()
    a.close()
   # return data


# get list id, name, address, county for admin edit section
def get_List_Edit_info():
    conn = connect()
    a = conn.cursor()
    try:
        _SQL = ('SELECT listing.id,listing.name,listing.address,county.county FROM `listing` inner join county on listing.id = county.id')
        a.execute(_SQL)
        data = a.fetchall()
        d = []
        for listing in data:
            d.append({'id': listing[0],
                      'name': listing[1],
                      'address': listing[2],
                      'county': listing[3]
                     })
        data = d



    except:
        data = 'fail'
    a.close()
    return data



# get (multiple) listing data for card display by type and county
# takes list type title and county as argument in URL
def get_card_data(title, county):
    conn = connect()
    a = conn.cursor()
    # avoid sql injection
    county = conn.escape_string(str(county))
    title = conn.escape_string(str(title))
    try:
        # check if title is in listtype table
        _SQL = ('SELECT id  from listtype WHERE title = "' + title + '"')
        result = a.execute(_SQL)
        # if the row was found
        if result is not 0:
            _SQL = "select listing.id, listing.image, listing.name, listing.latitude, listing.longitude from listing\
             inner join listtype on listing.listTypeID = listtype.id inner join county on listing.countyID = county.id\
             where county.county = '"+county+"' and listtype.title = '"+title+"' and listing.active = 1"
            a.execute(_SQL)
            data = a.fetchall()
            data = pares_sublisting_card_data(data)
        else:
            data = 'No title found'
    except:
        data = 'fail'
    a.close()
    return data


# get all (multiple) listings information by county, category and type
# takes listing type, category and county as argument in URL
def get_all_type_by_county_category(county, category, list_type):
    data = []
    conn = connect()
    a = conn.cursor()
    # avoid sql injection
    county = conn.escape_string(str(county))
    category = conn.escape_string(str(category))
    list_type = conn.escape_string(str(list_type))
    try:
        _SQL = ("SELECT listing.id,listing.name,listing.address,listing.text,listing.phone,listing.email,listing.image,\
        listing.latitude,listing.longitude FROM listing inner join county on listing.countyID = county.id\
        inner join listtype on listing.listTypeID = listtype.id inner join catagories on listtype.catID = catagories.id\
        where county.county = '"+county+"' and catagories.title = '"+category+"' and listtype.title = '"
        +list_type+"' and listing.active = 1")
        a.execute(_SQL)
        data = a.fetchall()
        d = []
        for listing in data:
            d.append({'id': listing[0],
                      'name': listing[1],
                      'address': listing[2],
                      'text': listing[3],
                      'phone': listing[4],
                      'email': listing[5],
                      'image': listing[6],
                      'latitude': listing[7],
                      'longitude': listing[8]})
        data = d
    except:
        data = 'fail'
    a.close()
    return data


# get comments and userNames for a listing
# takes listing id  as argument in URL
def get_all_comments_for_listing(listing_id):
    conn = connect()
    a = conn.cursor()
    # avoid sql injection
    listing_id = conn.escape_string(str(listing_id))
    try:
        # check if listing is in the listing table
        _SQL = ('SELECT id  from listing WHERE id = "' + listing_id + '"')
        result = a.execute(_SQL)
        # if the row was found
        if result is not 0:
            _SQL = ('SELECT commentrating.comment, users.userName, commentrating.id FROM commentrating\
                    inner join users on commentrating.userID = users.id\
                    inner join listing on commentrating.listingID = listing.id\
                    where listing.id = '+listing_id+' and commentrating.active = 1')
            a.execute(_SQL)
            data = a.fetchall()
            d = []
            for listing in data:
                d.append({'comment': listing[0],
                          'user': listing[1],
                          'id': listing[2],})
            data = d
        else:
            data = 'listing not found'
    except:
        data = 'fail'
    a.close()
    return data







#########################################################################################################

#def get_rating_listing(listing_id):


#########################################################################################################


# get all media links for a listing
# takes listings id as argument in URL
def get_medialinks_for_listing(listing_id):
    data = []
    conn = connect()
    a = conn.cursor()
    # avoid sql injection
    listing_id = conn.escape_string(str(listing_id))
    try:
        # check if listing is in the listing table
        _SQL = ('SELECT id  from listing WHERE id = "' + listing_id + '"')
        result = a.execute(_SQL)
        # if the row was found
        if result is not 0:
            _SQL = ('select medialinks.website,medialinks.facebook,medialinks.twitter,medialinks.instagram from medialinks\
            inner join listing on medialinks.listingID = listing.id where medialinks.listingID = '
            +listing_id+' and listing.active = 1')
            a.execute(_SQL)
            data = a.fetchall()
            d = []
            for listing in data:
                d.append({'website': listing[0],
                          'facebook': listing[1],
                          'twitter': listing[2],
                          'instagram': listing[3]})
            data = d
        else:
            # the row was not found and zero was returned
            data = 'no result found'
    except:
        data = 'fail'
    a.close()
    return data


# get a users favorites list
# takes users id as argument in URL
def get_favorites_for_user(user_id):
    data = []
    conn = connect()
    a = conn.cursor()
    # avoid sql injection
    user_id = conn.escape_string(str(user_id))
    try:
        # check if user is in the users table
        _SQL = ('SELECT id from `users` WHERE id = "' + user_id + '"')
        result = a.execute(_SQL)
        # if the row was found
        print(result)
        if result is not 0:
            _SQL = ('SELECT listing.image,listing.name,listing.longitude,listing.latitude from listing\
             inner join favorites on listing.id = favorites.listingID where favorites.userID = '
            +user_id+' and favorites.active = 1')
            a.execute(_SQL)
            data = a.fetchall()
            d = []
            for listing in data:
                d.append({'image': listing[0],
                          'listing_name': listing[1],
                          'longitude': listing[2],
                          'latitude': listing[3]})
            data = d
        else:
            # the row was not found and zero was returned
            data = 'no result found'
    except:
        data = 'fail'
    a.close()
    return data


# get the view count for a listing
# takes listing id as argument in URL
def view_count(list_id):
    data = []
    conn = connect()
    a = conn.cursor()
    # avoid sql injection
    list_id = conn.escape_string(str(list_id))
    try:
        # check if listing is in the listing table
        _SQL = ('SELECT id from `listing` WHERE id = "'+list_id+'"')
        result = a.execute(_SQL)
        # if the row was found
        if result is not 0:
            _SQL = ('SELECT view_count from `listing` WHERE id = "'+list_id+'"')
            a.execute(_SQL)
            conn.commit()
            data = a.fetchall()
            d = []
            for listing in data:
                d.append({'view_count': listing[0]})
            data = d
        else:
            # the row was not found and zero was returned
            data = 'no result found'
    except ValueError as v:
        data = 'fail'
    a.close()
    return data


# get (multiple) nearby places id for a listing
# takes listing id as argument in URL
def get_nearby_listings(list_id):
    conn = connect()
    a = conn.cursor()
    # avoid sql injection
    list_id = conn.escape_string(str(list_id))
    try:
        # check if listing is in the listing table
        _SQL = ('SELECT id from nearby WHERE listingID = "'+list_id+'"')
        result = a.execute(_SQL)
        # if the listing was found
        if result is not 0:
            # get all relatedListingID for a listing
            _SQL = ('SELECT relatedListingID from nearby WHERE listingID = "'+list_id+'" and active = 1')
            a.execute(_SQL)
            conn.commit()
            data = a.fetchall()
            d = []
            for listing in data:
                d.append({'relatedID': listing[0]})
            data = d
        else:
            # the row was not found and zero was returned
            data = 'no results found'
    except ValueError as v:
        data = 'fail'
    a.close()
    return data


##############################################################
#                           POST
##############################################################


# Add image to posted data's table in DB - all images should be added through this method
def add_image_to_DB(path,table,id):
    conn = connect()
    a = conn.cursor()
    try:
        path = path.replace('\\','\\\\') # prepare string for DB by adding two backslashes
        _SQL = ('UPDATE ' + str(table) + ' SET image = "'+ str(path) +'" where id = ' + str(id))
        a.execute(str(_SQL))
        conn.commit()
        msg = 'image successful added'
    except ValueError as v:
        conn.rollback()
        msg = 'fail'
    a.close()
    return msg


# TAKES POST JSON FROM CLIENT
# create a new listing to add to the database
def create_listing(data):
    conn = connect()
    a = conn.cursor()
    # avoid sql injection
    list_type_id = conn.escape_string(str(data['list_type_id']))
    county_id = conn.escape_string(str(data['county_id']))
    name = conn.escape_string(str(data['name']))
    address = conn.escape_string(str(data['address']))
    latitude = conn.escape_string(str(data['latitude']))
    longitude = conn.escape_string(str(data['longitude']))
    text = conn.escape_string(str(data['text']))
    phone = conn.escape_string(str(data['phone']))
    email = conn.escape_string(str(data['email']))
    website = conn.escape_string(str(data['website']))
    facebook = conn.escape_string(str(data['facebook']))
    twitter = conn.escape_string(str(data['twitter']))
    instagram = conn.escape_string(str(data['instagram']))
    try:
        # check if listing is in the listing table and active is set to zero
        _SQL1 = ('select name, address, phone,latitude,longitude,countyID from listing WHERE name = "'+name+'" and address = "'+address+'" and phone = "'
                 +phone+'" and latitude = "'+latitude+'" and longitude = "'+longitude+'" and countyID = "'+county_id+'"')
        result = a.execute(_SQL1)
        # if listing is not already in the database
        if result is 0:
            _SQL = ('INSERT INTO listing (name,address,latitude,longitude,text,phone,email,listTypeID,\
            countyID) VALUES ("'+name+'","'+address+'","'+latitude+'","'+longitude+'","'
            +text+'","'+phone+'","'+email+'","'+list_type_id+'","'+county_id+'")')
            a.execute(_SQL)
            conn.commit()
            a.execute('SELECT LAST_INSERT_ID()')
            result = a.fetchall()
            _SQL2 = ('INSERT INTO medialinks (listingID,website,facebook,twitter,instagram) \
                    VALUES ("' + str(result[0][0]) + '","' + website + '","' + facebook + '","' + twitter + '","'
                    + instagram + '")')
            a.execute(_SQL2)
            conn.commit()
            msg = result[0][0]
        else:
            msg = 'not a valid request - listing may already exist'
    except ValueError as v:
        conn.rollback()
        msg = 'fail'
    a.close()
    return msg


# TAKES POST JSON FROM CLIENT
#add new list type
def add_new_list_type(data):
    conn = connect()
    a = conn.cursor()
    # avoid sql injection
    list_type = conn.escape_string(str(data['type']))
    image = conn.escape_string(str(data['image']))
    cat_id = conn.escape_string(str(data['catID']))
    try:
        # check if the list type is in the listtype table
        _SQL = ('select id from listtype WHERE title = "' + list_type + '"')
        result = a.execute(_SQL)
        # if the row was not found
        if result is 0:
            _SQL = ('INSERT INTO listtype (title,image,catID) VALUES ("'+list_type+'","'+image+'","'+cat_id+'")')
            a.execute(_SQL)
            conn.commit()
            msg = 'New list title add'
        else:
            # the row was found
            msg = 'title already exist'
    except ValueError as v:
        # sql query has an error or something went wrong
        conn.rollback()
        msg = 'fail'
    a.close()
    return msg


# TAKES POST JSON FROM CLIENT
# add a user rating to a listing
def create_rating(data):
    conn = connect()
    a = conn.cursor()
    # avoid sql injection
    list_id = conn.escape_string(str(data['list_id']))
    user_id = conn.escape_string(str(data['user_id']))
    rating = conn.escape_string(str(data['rating']))
    try:
        # check if listing is in the listing table and active is set to zero
        _SQL1 = ('select id from listing WHERE id = "' + list_id + '" and active=1')
        result1 = a.execute(_SQL1)
        # check if user is in the listing table and active is set to zero
        _SQL2 = ('select id from users WHERE id = "' + user_id + '" and active=1 ')
        result2 = a.execute(_SQL2)
        # if user and listing are valid
        if result1 > 0 and result2 > 0:
            # check if listing has a rating already by the user
            #select id from commentrating WHERE listingID = 4 and userID = 1
            _SQL3 = ('select id from commentrating WHERE listingID ='+list_id+' and userID = '+user_id)
            result3 = a.execute(_SQL3)
            if result3 > 0:
                # get commentrating row id
                data = a.fetchall()
                # up-date listing rating
                _SQL4 = ('UPDATE commentrating SET rating = "'+rating+'" WHERE id ="'+str(data[0][0])+'"')
                a.execute(_SQL4)
                conn.commit()
                msg = 'rating updated'
            else:
                # first time for user to rate listing
                _SQL5 = ('INSERT INTO commentrating (`listingID`,`userID`,`rating`) VALUES ("' + list_id + '","' + user_id + '","' + rating + '")')
                a.execute(_SQL5)
                conn.commit()
                msg = 'rating added'
        else:
            # no record found
            msg = 'not a valid request'
    except ValueError as v:
        conn.rollback()
        msg = 'fail'
    a.close()
    return msg


# TAKES POST JSON FROM CLIENT
# add a user comment to a listing
def create_comment(data):
    conn = connect()
    a = conn.cursor()
    # avoid sql injection
    list_id = conn.escape_string(str(data['list_id']))
    user_id = conn.escape_string(str(data['user_id']))
    comment = conn.escape_string(str(data['comment']))
    try:
        # check if listing is in the listing table and active is set to zero
        _SQL1 = ('select id from listing WHERE id = "' + list_id + '" and active=1')
        result1 = a.execute(_SQL1)
        # check if user is in the listing table and active is set to zero
        _SQL2 = ('select id from users WHERE id = "' + user_id + '" and active=1 ')
        result2 = a.execute(_SQL2)
        # if user and listing are valid
        if result1 > 0 and result2 > 0:
            # check if listing has a comment already by the user
            _SQL3 = ('select id from commentrating WHERE listingID =' + list_id + ' and userID = ' + user_id)
            result3 = a.execute(_SQL3)
            if result3 > 0:
                # get commentrating row id
                data = a.fetchall()
                # up-date listing rating
                _SQL4 = ('UPDATE commentrating SET comment = "' + comment + '" WHERE id ="' + str(data[0][0]) + '"')
                a.execute(_SQL4)
                conn.commit()
                msg = 'comment updated'
            else:
                # both comment and rating entered
                _SQL = ('INSERT INTO commentrating (`listingID`,`userID`,`comment`) VALUES ("' + list_id + '","' + user_id + '","' + comment + '")')
                a.execute(_SQL)
                conn.commit()
                msg = 'comment added'
        else:
            # no record found
            msg = 'not a valid request'
    except ValueError as v:
        conn.rollback()
        msg = 'fail'
    a.close()
    return msg


# TAKES POST JSON FROM CLIENT
# add a listing to a users favorites list
def add_listing_to_users_favorites(data):
    conn = connect()
    a = conn.cursor()
    # avoid sql injection
    list = conn.escape_string(str(data['list_id']))
    user = conn.escape_string(str(data['user_id']))
    try:
        # check if user and list are in the favorites table
        _SQL = ('select userID, listingID from favorites WHERE userID = "' + user + '" and listingID="' + list + '"')
        result1 = a.execute(_SQL)
        # check if listing is valid
        _SQL2 = ('select id from listing WHERE id="'+list+'"')
        result2 = a.execute(_SQL2)
        print(result1, result2)
        # if the row was not found
        if result1 is 0:
            if result2 > 0:
                _SQL = ('INSERT INTO favorites (`userID`,`listingID`) VALUES ('+user+','+list+')')
                a.execute(_SQL)
                conn.commit()
                msg = 'listing added to users favorites list'
            else:
                # listing is not valid
                msg = 'listing is not valid'
        else:
            # the row was not found and zero was returned
            msg = 'listing already in favorites'
    except ValueError as v:
        conn.rollback()
        msg = 'fail'
    a.close()
    return msg


# TAKES POST JSON FROM CLIENT
# remove a listing from the users favorites list
def remove_listing_to_users_favorites(data):
    conn = connect()
    a = conn.cursor()
    # avoid sql injection
    list = conn.escape_string(str(data['list_id']))
    user = conn.escape_string(str(data['user_id']))
    try:
        # check if user and list are in the favorites table
        _SQL = ('select userID, listingID from favorites WHERE userID = "' + user + '" and listingID="' + list + '"')
        result = a.execute(_SQL)
        # if the row was found
        if result is not 0:
            _SQL = ('UPDATE favorites SET active="0" WHERE userID = "'+user+'" and listingID="'+list+'"')
            a.execute(_SQL)
            conn.commit()
            msg = 'listing removed from users favorites list'
        else:
            # the row was not found and zero was returned
            msg = 'no result found'
    except ValueError as v:
        # sql query has an error or something went wrong
        conn.rollback()
        msg = 'fail'
    a.close()
    return msg


# TAKES POST JSON FROM CLIENT
# report a comment
def report_comment(data):
    conn = connect()
    a = conn.cursor()
    # avoid sql injection
    commentID = conn.escape_string(str(data['commentID']))
    try:
        # check if the comment is in the commentrating table
        _SQL = ('select id from commentrating WHERE id = "' + commentID + '" and active = 1 ')
        result = a.execute(_SQL)
        # if row found
        if result is not 0:
            # check if the comment has already been reported and not dealt with
            _SQL = ('select id from reportbadbehaviour WHERE commentID = "' + commentID + '" and attendedTo = 0 ')
            result = a.execute(_SQL)
            # if row not found
            print(result)
            if result is 0:
                _SQL = ('INSERT INTO reportbadbehaviour(commentID) VALUES ("'+commentID+'")' )
                a.execute(_SQL)
                conn.commit()
                msg = 'comment has been reported'
            else:
                _SQL = ('UPDATE reportbadbehaviour SET reportedAmount = reportedAmount + 1 WHERE commentID = "'+commentID+'" and attendedTo = 0')
                a.execute(_SQL)
                conn.commit()
                msg = 'reported'
        else:
            # no record found
            msg = 'no comment found'
    except ValueError as v:
        conn.rollback()
        msg = 'fail'
    a.close()
    return msg


# TAKES POST JSON FROM CLIENT
# update a single listing
def update_listing(data):
    conn = connect()
    a = conn.cursor()
    # avoid sql injection
    id = conn.escape_string(str(data['id']))
    name = conn.escape_string(str(data['name']))
    address = conn.escape_string(str(data['address']))
    latitude = conn.escape_string(str(data['latitude']))
    longitude = conn.escape_string(str(data['longitude']))
    text = conn.escape_string(str(data['text']))
    phone = conn.escape_string(str(data['phone']))
    email = conn.escape_string(str(data['email']))
    listTypeID = conn.escape_string(str(data['listTypeID']))
    countyID = conn.escape_string(str(data['countyID']))
    try:
        # check if listing is in the listing table
        _SQL = ('select id from listing WHERE id = "' + id + '"')
        result = a.execute(_SQL)
        # if the row was found
        if result is not 0:
            _SQL = ('UPDATE listing SET name="'+name+'",address="'+address+'",latitude="'+latitude+'",\
            longitude="'+longitude+'",text="'+text+'",phone="'+phone+'",email="'+email+'"listTypeID="'+listTypeID+'",\
            countyID="'+countyID+'" WHERE id = "'+id+'"')
            a.execute(_SQL)
            conn.commit()
            _SQL2 = ('INSERT INTO medialinks (listingID,website,facebook,twitter,instagram) \
                    VALUES ("' + id + '","' + website + '","' + facebook + '","' + twitter + '","'+ instagram + '")')
            a.execute(_SQL2)
            conn.commit()
            msg = 'listing updated'
        else:
            # the row was not found
            msg = 'listing not found'
    except ValueError as v:
        # sql query has an error or something went wrong
        conn.rollback()
        msg = 'fail'
    a.close()
    return msg




"""
get events
get visit carlow data : media links, terms of use, logo....
register user, change password, login, logout
# get average rating for a listing - calc all ? (should return one overall rating)
"""