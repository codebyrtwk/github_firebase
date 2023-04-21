from rest_framework import viewsets
from rest_framework.response import Response
from github import Github
from .models import Repository 
from .serializers import RepositorySerializer 
import firebase_admin
from firebase_admin import firestore , credentials

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = GitUser.objects.all()
#     serializer_class = UserSerializer

#     # @action(detail=True, methods=['get'])
#     # def repositories(self, request, pk=None):
#     #     user = self.get_object()
#     #     repositories = user.repositories.all()
#     #     serializer = RepositorySerializer(repositories, many=True)
#     #     return Response(serializer.data)
    

class RepositoryViewSet(viewsets.ModelViewSet):
    def list(self, request  ):
        # Pull data from GitHub
        g = Github()
        username = request.data['username'] # basically its response payload
        user = g.get_user(username)
        print(user.login)
        repos = [{'ownername': repo.owner.login,"title":repo.name, 'description': repo.description , "url": repo.url} for repo in user.get_repos()]
        print(repos)
        # Save data to Firebase
        print("---------------FIREBASE CLIENT---------------" , firestore.client)
        cred = credentials.Certificate('github_firebase_ap\githubfirebase-44f2c-firebase-adminsdk-ixhhe-63b826d461.json')
        firebase_admin.initialize_app(cred)
        db = firestore.client()
        print(db)
        print("21_________________")
        for repo in repos:
            data = {'ownername': repo['ownername'], "title": repo["title"], 'description': repo['description'] , "url":repo['url']}
            if Repository.objects.filter(ownername=username).exists():
                # If username already exists, print this
                # print('Username already exists')
                print("It already exist in firestore")
            else:
                data_ref = db.collection('repositories').document()
                data_ref.set(data)
                print("uploaded")
        docs = db.collection('repositories').get()
        print("48________________",docs)
        for doc in docs:
            print(doc.id, doc.to_dict())
        print("Create repository to firestore-------------------")
        # Save data to Django model if new username is entered only     
        if Repository.objects.filter(ownername=username).exists() :
            # If username already exists, print this
            print('Username already exists')
        else:
            Repository.objects.bulk_create([Repository(ownername=repo['ownername'],title = repo["title"], description=repo['description'] , url=repo['url']) for repo in repos])
        # Retrieve data from Django model and serialize to JSON
        queryset = Repository.objects.filter(ownername = username)
        serializer = RepositorySerializer(queryset, many=True)
        return Response(serializer.data)
