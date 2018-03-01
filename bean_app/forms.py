from django import forms

from bean_app.models import Tag, CoffeeBean, Customer, Review, Vendor


class Tag(forms.ModelForm):
    name = forms.CharField(max_length=128,
                           help_text="Please enter the Tag name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Tag
        fields = ('name',)


# class CoffeeBean(forms.ModelForm):
#     title = forms.CharField(max_length=128,
#                             help_text="Please enter the Coffee Bean title.")
#     url = forms.CharField(max_length=200,
#                           help_text="Please enter the URL of the page.")
#     views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
#
#     class Meta:
#         model = CoffeeBean
#         exclude = ('category',)
#
#     def clean(self):
#         cleaned_data = self.cleaned_data
#         url = cleaned_data.get('url')
#
#         if url and not url.startswith('http://'):
#             url = 'http://' + url
#             cleaned_data['url'] = url
#             return cleaned_data


        # class Customer(forms.ModelForm):
        #     class Meta:
        #         model = Customer
        #         fields = ('',)

        #
        # class Review(forms.ModelForm):
        #     class Meta:
        #         model = Review
        #         fields = ('',)

        #
        # class Vendor(forms.ModelForm):
        #     class Meta:
        #         model = Review
        #         fields = ('',)

        #
        # class VendorSignupForm(forms.ModelForm):
        #     password = forms.CharField(widget=forms.PasswordInput())
        #
        #     class Meta:
        #         model = Vendor
        #         fields = ('Full Name', 'Full Address', 'Contact', 'Shop or Cafe URL', 'email', 'password', 'Password(repeat)')


        # class SignupForm(forms.ModelForm):

        #    email = forms.CharField(widget=forms.EmailInput())
        # password = forms.CharField(widget=forms.PasswordInput())
        # password_repeat = forms.CharField(widget=forms.PasswordInput())

        #    class Meta:
        # model = User
        # fields = ('email', 'password', 'password_repeat')


        # class MyAccountForm(forms.ModelForm):
        #     class Meta:
        #         model = MyAccountForm
        #         fields = ('FullName', 'Address', 'Contact', 'Favourite', 'email', 'password', 'Password(repeat)')

        #
        # class UserAccountPicture(forms.ModelForm):
        #     class Meta:
        #         model = UserAccountPicture
        #         fields = ('website', 'picture')
        #
        #
        # class UserAccountPicture(forms.ModelForm):
        #     class Meta:
        #         model = UserAccountPicture
        #         fields = ('website', 'picture')
        #

        # class UserForm(forms.ModelForm):
        #   password = forms.CharField(widget=forms.PasswordInput())

        # class Meta:
        # model = User
        # fields = ('email', 'password')
