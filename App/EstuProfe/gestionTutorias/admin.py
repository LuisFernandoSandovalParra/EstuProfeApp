from django.contrib import admin

from gestionTutorias.models import Users, Publications, PublicationsTutors, Tutorships, TutorsInterests, Tutors, Students, Interests

# Register your models here.
#----------------------------------------------------listos------------------------------------------------------------
class UsersAdmin(admin.ModelAdmin):
    list_display =("user_id", "email", "type")
    search_fields =("user_id", "email", "type")
    list_filter =("user_id", "email")

class PersonalInformationAdmin(admin.ModelAdmin):
    list_display =("document_id", "first_name", "last_name", "birthdate", "gender", "phone_number", "education_level")
    search_fields =("document_id", "first_name", "last_name", "birthdate", "gender", "phone_number", "education_level")
    list_filter =("gender", "education_level")

class PublicationsAdmin(admin.ModelAdmin):
    list_display =("publication_id", "publication_date", "deadline", "area", "is_accepted", "student")
    search_fields =("publication_id", "publication_date", "deadline", "area", "is_accepted")
    list_filter = ("area", "is_accepted", "publication_date", "deadline")
class PublicationsTutorsAdmin(admin.ModelAdmin):
    list_display =("tutor", "publication", "time", "value")
    search_fields =("time", "value")
    #publication, publication_id, publication_tutor_id, time, user_tutor, user_tutor_id, value

class TutorshipsAdmin(admin.ModelAdmin):
    list_display =("tutorship_id", "tutorship_date", "hour", "student", "tutor")
    search_fields = ("tutorship_id", "tutorship_date", "hour")
    list_filter = ("tutorship_date",)

class TutorsInterestsAdmin(admin.ModelAdmin):
    list_display=("interest", "tutor")
    search_fields = ("interest",)
    list_filter = ("interest",)

class TutorsAdmin(admin.ModelAdmin):
    list_display = ("tutor_id","document","user")
    search_fields = ("tutor_id",)

class StudentsAdmin(admin.ModelAdmin):
    list_display = ("student_id","document","user")
    search_fields = ("student_id",)

class InterestsAdmin(admin.ModelAdmin):
    list_display = ("interest_id","area")
    search_fields = ("interest_id", "area")
    list_filter = ("area",)
#-----------------------------------------------------------------------------------------------------------------------



admin.site.register(Users, UsersAdmin)
admin.site.register(Publications, PublicationsAdmin)
admin.site.register(PublicationsTutors, PublicationsTutorsAdmin)
admin.site.register(Tutorships, TutorshipsAdmin)
admin.site.register(TutorsInterests, TutorsInterestsAdmin)
admin.site.register(Tutors, TutorsAdmin)
admin.site.register(Students, StudentsAdmin)
admin.site.register(Interests, InterestsAdmin)


