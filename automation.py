{
	"info": {
		"_postman_id": "41ae5492-3fbd-4a15-984b-d658b9f9d749",
		"name": "AccuKnox",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
		"_exporter_id": "4093302"
	},
	"item": [
		{
			"name": "sign in",
			"request": {
				"auth": {
					"type": "bearer",
					"bearer": [
						{
							"key": "token",
							"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg1NzQyNjkyLCJpYXQiOjE2ODU3NDE3OTIsImp0aSI6ImJkZWJkYTYyMjEzNDQzNjZiNGE5MGIwNmIxYWVmZmY0IiwidXNlcl9pZCI6MX0.fEvI_YCRUZ4TsiJ500haDG8apBECJRDTkGy6fn5UDGk",
							"type": "string"
						}
					]
				},
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\r\n    \"target_price\":27168,\r\n    \"currency_id\":1\r\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:8000/alerts/create/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"alerts",
						"create",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "sign up",
			"request": {
				"method": "GET",
				"header": []
			},
			"response": []
		},
		{
			"name": "search users",
			"request": {
				"method": "GET",
				"header": []
			},
			"response": []
		},
		{
			"name": "friend request send",
			"request": {
				"method": "GET",
				"header": []
			},
			"response": []
		},
		{
			"name": "friend request, accept-reject",
			"protocolProfileBehavior": {
				"disableBodyPruning": true
			},
			"request": {
				"auth": {
					"type": "bearer",
					"bearer": [
						{
							"key": "token",
							"value": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg4MTM1MzE5LCJpYXQiOjE2ODgwNDg5MTksImp0aSI6IjExMWQ3N2U2Y2IyNTRmY2FiZDZiOGM3NzM2OTVjN2I4IiwidXNlcl9pZCI6MjJ9.JlFI1omj0KzL-2wckf3wmzoln5gZZuHSTDoAKC3BCzg",
							"type": "string"
						}
					]
				},
				"method": "GET",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\r\n\"request_id\" : 16,\r\n\"is_accepted\" : true\r\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://localhost:8000/friend-request/accept/",
					"protocol": "http",
					"host": [
						"localhost"
					],
					"port": "8000",
					"path": [
						"friend-request",
						"accept",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "list friends",
			"protocolProfileBehavior": {
				"disableBodyPruning": true
			},
			"request": {
				"auth": {
					"type": "bearer",
					"bearer": [
						{
							"key": "token",
							"value": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg4MTM1MzE5LCJpYXQiOjE2ODgwNDg5MTksImp0aSI6IjExMWQ3N2U2Y2IyNTRmY2FiZDZiOGM3NzM2OTVjN2I4IiwidXNlcl9pZCI6MjJ9.JlFI1omj0KzL-2wckf3wmzoln5gZZuHSTDoAKC3BCzg",
							"type": "string"
						}
					]
				},
				"method": "GET",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\r\n\"request_id\" : 16,\r\n\"is_accepted\" : true\r\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://localhost:8000/friend-request/accept/",
					"protocol": "http",
					"host": [
						"localhost"
					],
					"port": "8000",
					"path": [
						"friend-request",
						"accept",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "pending request list",
			"protocolProfileBehavior": {
				"disableBodyPruning": true
			},
			"request": {
				"auth": {
					"type": "bearer",
					"bearer": [
						{
							"key": "token",
							"value": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg4MTM1MzE5LCJpYXQiOjE2ODgwNDg5MTksImp0aSI6IjExMWQ3N2U2Y2IyNTRmY2FiZDZiOGM3NzM2OTVjN2I4IiwidXNlcl9pZCI6MjJ9.JlFI1omj0KzL-2wckf3wmzoln5gZZuHSTDoAKC3BCzg",
							"type": "string"
						}
					]
				},
				"method": "GET",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\r\n\"request_id\" : 16,\r\n\"is_accepted\" : true\r\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://localhost:8000/friend-request/accept/",
					"protocol": "http",
					"host": [
						"localhost"
					],
					"port": "8000",
					"path": [
						"friend-request",
						"accept",
						""
					]
				}
			},
			"response": []
		}
	]
}