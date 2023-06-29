steps for setup:

1# poetry install 
2#  docker-compose up -d
3# python manage.py runserver


postman collection is added with filename :
 automation.py (also AccuKnox.postman_collection.json)

also i am adding curl requests of each apis

1#  sign in 

curl --location 'http://localhost:8000/signin/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg1NzQyNjkyLCJpYXQiOjE2ODU3NDE3OTIsImp0aSI6ImJkZWJkYTYyMjEzNDQzNjZiNGE5MGIwNmIxYWVmZmY0IiwidXNlcl9pZCI6MX0.fEvI_YCRUZ4TsiJ500haDG8apBECJRDTkGy6fn5UDGk' \
--data-raw '{
    "email":"11rahu1l2@rahu1.COM",
    "password":"Test123",
    "first_name":"Rahu",
    "last_name":"Test123"
}'



2#   signup

curl --location 'http://localhost:8000/signup/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email":"11rahu11l2@rahu1.COM",
    "password":"Test123",
    "first_name":"Rahu",
    "last_name":"Test123"
}'



3#  search users

curl --location 'http://localhost:8000/user/search/?search_keyword=aaaa' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg4MTUzODMxLCJpYXQiOjE2ODgwNjc0MzEsImp0aSI6IjdmODY5MGU1ZTM0MDQ0MWViNDNiYTc3NDZlOTk4YzBlIiwidXNlcl9pZCI6MjN9.433p2yNssRFkr5m_U7WiTd4ibbqxVNgOEQiFlHDsHPo'

4#  send the friend request


curl --location 'http://localhost:8000/friend-request/send/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg4MTM1MzE5LCJpYXQiOjE2ODgwNDg5MTksImp0aSI6IjExMWQ3N2U2Y2IyNTRmY2FiZDZiOGM3NzM2OTVjN2I4IiwidXNlcl9pZCI6MjJ9.JlFI1omj0KzL-2wckf3wmzoln5gZZuHSTDoAKC3BCzg' \
--data '{
"user_id" : 1

}'

5#  accept the request


curl --location 'http://localhost:8000/friend-request/accept/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg4MTM1MzE5LCJpYXQiOjE2ODgwNDg5MTksImp0aSI6IjExMWQ3N2U2Y2IyNTRmY2FiZDZiOGM3NzM2OTVjN2I4IiwidXNlcl9pZCI6MjJ9.JlFI1omj0KzL-2wckf3wmzoln5gZZuHSTDoAKC3BCzg' \
--data '{
"request_id" : 18,
"is_accepted" : true
}'


6#  get all friends list

curl --location 'http://localhost:8000/friends/list/' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg4MTM1MzE5LCJpYXQiOjE2ODgwNDg5MTksImp0aSI6IjExMWQ3N2U2Y2IyNTRmY2FiZDZiOGM3NzM2OTVjN2I4IiwidXNlcl9pZCI6MjJ9.JlFI1omj0KzL-2wckf3wmzoln5gZZuHSTDoAKC3BCzg' \
--data ''


7#  pending requests

curl --location 'http://localhost:8000/friend-request/pending/list/' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg4MTM1MzE5LCJpYXQiOjE2ODgwNDg5MTksImp0aSI6IjExMWQ3N2U2Y2IyNTRmY2FiZDZiOGM3NzM2OTVjN2I4IiwidXNlcl9pZCI6MjJ9.JlFI1omj0KzL-2wckf3wmzoln5gZZuHSTDoAKC3BCzg' \
--data ''