from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = [
            "title",
            "description",
            "price"
        ]

#pure django form not model form
#passing this in view as an instance can get us send a form to a user and get a post back
class RawProductForm(forms.Form):
    title =         forms.CharField()
    description =   forms.CharField()
    price =         forms.DecimalField()


class RawProductFormWith_properties(forms.Form):
    title =         forms.CharField(
                        # label='',
                        max_length = 120, 
                        required = True, 
                        widget=forms.TextInput(
                                attrs = {
                                    'class':'form-control',
                                    'type':'text',
                                    'placeholder':'field',
                                }

    )) #labe='' will take the label away
    description =   forms.CharField(
                            required=False,
                            widget=forms.Textarea(
                                attrs={
                                    "class" : "new-class-name two",
                                    "id" : "my-id-for-textare",
                                    "row":20,
                                    "col" : 120,
                                }
                            )
                    ) #means this will be skipped
    price =         forms.DecimalField(initial=192) #giving it initial value

class ProductFormOveride(forms.ModelForm):
    email =         forms.EmailField( required=False)
    title =         forms.CharField(
                        # label='',
                        max_length = 120, 
                        required = True, 
                        widget=forms.TextInput(
                                attrs = {
                                    'class':'form-control',
                                    'type':'text',
                                    'placeholder':'field',
                                }

    )) #labe='' will take the label away
    description =   forms.CharField(
                            required=False,
                            widget=forms.Textarea(
                                attrs={
                                    "class" : "new-class-name two",
                                    "id" : "my-id-for-textare",
                                    "row":20,
                                    "col" : 120,
                                }
                            )
                    ) #means this will be skipped
    
    class Meta:
        model = Product
        fields = [
            "title",
            "description",
            "email",     #renders in a form in template even though there is no place in db
            "price"
        ]

    # def clean_title(self, *args, **kwargs):
    #     title = self.cleaned_data.get("title")
    #     if not "CFE" in title:
    #         raise forms.ValidationError("Thi is not valid")
    #     # if not "Chelsea" in title:
    #     #     raise forms.ValidationError("Not valid title")
    #     return 
    
    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith("edu"):
            raise forms.ValidationError("This is not a valid email")
        return email
    