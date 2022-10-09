# from rest_framework import serializers
# from SIGNALS.models import signalsSubjectsModel
#
#
# class signalsAdminSubjectsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = signalsSubjectsModel
#         fields = "__all__"
#
# class siganlsAdminStudentSerializer(serializers.Serializer):
#     user_slug = serializers.CharField(max_length=100, required=True)
#     subject_slug = serializers.CharField(max_length=100, required=True)
#
#     class Meta:
#         fields = "__all__"
#
#     def create(self, validated_data):
#         # user=self.context['request'].user
#         user_slug = validated_data['user_slug']
#         subject_slug = validated_data['subject_slug']
#         print(user_slug, subject_slug)
