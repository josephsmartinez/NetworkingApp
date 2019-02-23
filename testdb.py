from linux_app import db
from linux_app.models import User, Host

db.create_all()
# user1 = User(username='castic', email='castic@fiu.edu', password='password')
# user2 = User(username='josemart', email='josemat@fiu.edu', password='password')
# host1 = Host(hardware='0A:0F:27:7f:2e:4a', parent_name='rr-ini07', parent_type='Switch', parent_port='Gi2/11', fingerprint='nomatch', address='99.100.67.100')
# host2 = Host(hardware='1A:0F:27:7f:2f:4a', parent_name='rz-ini07', parent_type='Switch',parent_port='Ci2/20', fingerprint='nomatch', address='10.999.67.100')
# db.session.add(user2)
# db.session.add(host1)
# db.session.add(host2)
# db.session.commit()
# print(User.query.all())
# print(Host.query.all())