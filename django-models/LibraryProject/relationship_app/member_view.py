from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

def is_member(user):
    # Check if the user is authenticated and has the "Member" role in their UserProfile.
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(is_member)
def member_view(request):
    return HttpResponse("Welcome, Member!")
