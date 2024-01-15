from rest_framework import status

from core.fixtures.user import user
from core.fixtures.post import post

class TestUserViewSet:
	endpoint = '/api/user/'

	def test_list(self, client, user):
		# An authenticated user should enable a list of all users

		client.force_authenticate(user=user)
		response = client.get(self.endpoint)

		assert response.status_code == status.HTTP_200_OK
		assert response.data['count'] == 1


	def test_retrieve(self, client, user):
		# An authenticated user can retrieve resources concerning a user
		client.force_authenticate(user=user)
		response = client.get(self.endpoint + str(user.public_id) + '/')

		assert response.status_code == status.HTTP_200_OK
		assert response.data['id'] == user.public_id.hex
		assert response.data['email'] == user.email
		assert response.data['username'] == user.username

	def test_create(self, client, user):
		# Users cannot create users directly with a POST request
		client.force_authenticate(user=user)
		data = {}
		response = client.post(self.endpoint, data)
		assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


	def test_update(self, client, user):
		# An authenticated user can update a user object with a PATCH request
		data = {
			"username": "test_userMod",
		}
		client.force_authenticate(user=user)
		response = client.patch(self.endpoint + str(user.public_id) + '/', data)

		assert response.status_code == status.HTTP_200_OK
		assert response.data['username'] == data['username']