from rest_framework import serializers

from .models import Articles

"""
    Class to define Article creation serializer
    takes in the author_id since an article is associated to a user
    title, body, draft (specifies if user is just storing the article
    to edit later), post (specifies if an article is finished on editing
    or is ready to be published )

"""


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    title = serializers.CharField()
    body = serializers.CharField()
    draft = serializers.BooleanField()
    posted = serializers.BooleanField()

    # Defines fields fron the  article that are to be saved
    class Meta:
        model = Articles
        fields = ["author", "title", "body", "draft", "posted"]

    # Method to save article data to the data base.
    def create(self, valid_data):
        article = Articles(**valid_data)
        article.save()
        return article

    # Method to update article on 'PUT' request
    def update(self, instance, validated_data):
        # Match key value pair in validated data to key value pair
        # in instance
        for (key, value) in validated_data.items():
            setattr(instance, key, value)
        # Save the instance to db
        instance.save()
        # Return the saved data for user to see that change was successfull
        return instance

    # Method to check if user is autorized to perform such action
    @staticmethod
    def check_user_authorization(user_data, article_id):
        chosen_article = Articles.objects.all().get(id=article_id)
        # Check if user is matches article id. If not raise error that user cannot 
        # edit other users article
        if chosen_article.author_id != user_data.id:
            raise serializers.ValidationError(
                {"message": "You are not the owner of the article, hence you can't update it"}
            )
        return user_data


"""
    Serializer to load all article fields for the user to view
"""


class ViewArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = '__all__'
