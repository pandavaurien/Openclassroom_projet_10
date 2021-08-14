from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django import forms
# from django.core.exceptions import ValidationError
# from django.contrib.auth.forms import ReadOnlyPasswordHashField
# from django.contrib.auth.models import Group

from .models import User


admin.site.register(User)







# class UserCreationForm(forms.ModelForm):
#     email = forms.EmailField(label='Email', widget=forms.EmailInput)
#     password1 = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Confirmer le mot de passe', widget=forms.PasswordInput)

#     class Meta:
#         model = Users
#         fields = ("first_name", "last_name", "email")


#     def clean_password2(self):
#         # Check that the two password entries match
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise ValidationError("Les mots de passe ne correspondent pas")
#         return password2

#     def save(self, commit=True):
#         # Save the provided password in hashed format
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user


# class UserChangeForm(forms.ModelForm):
#     """A form for updating users. Includes all the fields on
#     the user, but replaces the password field with admin's
#     disabled password hash display field.
#     """
#     password = ReadOnlyPasswordHashField()

#     class Meta:
#         model = Users
#         fields = ('first_name', 'last_name', 'email', 'password', 'is_active', 'is_admin')


# class UserAdmin(BaseUserAdmin):
#     # The forms to add and change user instances
#     form = UserChangeForm
#     add_form = UserCreationForm

#     # The fields to be used in displaying the User model.
#     # These override the definitions on the base UserAdmin
#     # that reference specific fields on auth.User.
#     list_display = ('first_name', 'last_name', 'email', 'is_admin')
#     list_filter = ('is_admin',)
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Personal info', {'fields': ('first_name', 'last_name')}),
#         ('Permissions', {'fields': ('is_admin',)}),
#     )
#     # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
#     # overrides get_fieldsets to use this attribute when creating a user.
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('password1', 'password2'),
#         }),
#     )
#     search_fields = ('email',)
#     ordering = ('email',)
#     filter_horizontal = ()


# admin.site.register(Users, UserAdmin)
# admin.site.unregister(Group)
