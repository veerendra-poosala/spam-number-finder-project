from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import  ListAPIView,DestroyAPIView

from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import ContactsModel 
from regApp.models import RegisterUserModel
from .serializers import ContactsSerializer

from django.contrib.auth.models import User



def home(request):
    try:
        user_id = request.user.id
        user = User.objects.get(pk=user_id)

        user_name = user.username
        return render(request,'base.html',{'name':user_name})
    except User.DoesNotExist:
        return render(request,'loginForm.html')

def base(request):
    return render(request,'base.html')

def navToCreateContactForm(request):
    return render(request,'addContact.html')

def navToEditContactForm(request):
    return render(request,'editContact.html')

class ListContactsView(ListAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    #queryset = ContactsModel.objects.all()
    serializer_class = ContactsSerializer
    def get_queryset(self):
        user_id = self.request.user.id
        queryset = ContactsModel.objects.filter(owner_name_id = user_id)
        return queryset


class CreateContactsView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ContactsSerializer

    def post(self, request):
        data = request.data
        data['owner_name'] = request.user.id 
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        #print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class RetrieveContactsView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, user_input):
        if len(user_input) == 10:
            try:
                
                objs = ContactsModel.objects.filter(phone_number=user_input)
                if objs:
                    
                    obj = objs.first()
                    
                    data = {
                        'contact_name':obj.contact_name,
                        'phone_number':obj.phone_number,
                        'email':obj.email,
                        'spam':obj.spam,
                        'message':'Object found'

                    }
                    
                    
                    return Response(data, status=200)
                else:
                    
                    try:
                        obj = RegisterUserModel.objects.get(phone_number=user_input)  
                        
                        data = {
                        'contact_name':obj.contact_name,
                        'phone_number':obj.phone_number,
                        'email':obj.email,
                        'spam':obj.spam,
                        'message':'Object found'

                    }
                    
                    
                        return Response(data, status=200)
                        
                    except RegisterUserModel.DoesNotExist:
                        return Response({'message': 'Object not found'})
            except ContactsModel.DoesNotExist:
                
                try:
                    obj = RegisterUserModel.objects.get(phone_number=user_input)  
                    data = {
                        'contact_name':obj.contact_name,
                        'phone_number':obj.phone_number,
                        'email':obj.email,
                        'spam':obj.spam,
                        'message':'Object found'

                    }
                    
                    return Response(data, status=200)
                except RegisterUserModel.DoesNotExist:
                    return Response({'message': 'Object not found'})
        else:
            return Response({'message': 'Object not found'})

        

class UpdateContactsView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ContactsSerializer
    def put(self,request,user_input):
        data = request.data
        data['owner_name'] = request.user.id

        try:
            contact = ContactsModel.objects.get(pk=int(user_input))
        except ContactsModel.DoesNotExist:
            return Response({'message': 'Contact not found.'}, status=404)

        serializer = self.serializer_class(contact,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return render(request,'base.html',{'message':'Updated Successfully'})
        else:
            
            return Response({"message":'Something went wrong'},status=400)
        

    

class DestroyContactsView(DestroyAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = ContactsModel.objects.all()
    serializer_class = ContactsSerializer
