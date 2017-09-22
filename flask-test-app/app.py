from flask import Flask,render_template,make_response,request



#request.headers.get('User-Agent')
#page=request.args.get('page')
#per_page=request.args.get('per_page')


app=Flask(__name__)
app.config.update({
    'SECRET_KEY':'a random string'
    })

@app.route('/')
def index():
    username=request.cookies.get('username')
    #return 'Hello World!'
    return 'Hello {}'.format(username)


@app.route('/user/<username>')
def user_index(username):
    #return 'Hello {}'.format(username)
    resp=make_response(render_template('user_index.html',username=username))
    resp.set_cookie('username',username)
    #return render_template('user_index.html',username=username)
    return resp

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post {}'.format(post_id)

if __name__=='__main__':
    app.run()

