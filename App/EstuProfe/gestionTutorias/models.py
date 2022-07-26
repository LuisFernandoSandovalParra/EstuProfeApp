from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Interests(models.Model):
    interest_id = models.AutoField(primary_key=True)
    area = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'interests'


class PersonalInformation(models.Model):
    document_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    birthdate = models.DateField()
    gender = models.CharField(max_length=19)
    phone_number = models.CharField(max_length=20)
    education_level = models.CharField(max_length=10)
    autobiography = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personal_information'


class Publications(models.Model):
    publication_id = models.AutoField(primary_key=True)
    publication_date = models.DateField()
    deadline = models.DateField()
    area = models.CharField(max_length=11)
    description = models.CharField(max_length=300)
    is_accepted = models.IntegerField()
    student = models.ForeignKey('Students', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'publications'


class PublicationsTutors(models.Model):
    tutor = models.OneToOneField('Tutors', models.DO_NOTHING, primary_key=True)
    publication = models.ForeignKey(Publications, models.DO_NOTHING)
    time = models.TimeField()
    value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'publications_tutors'
        unique_together = (('tutor', 'publication'),)


class Students(models.Model):
    student_id = models.AutoField(primary_key=True)
    document = models.ForeignKey(PersonalInformation, models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'students'


class Tutors(models.Model):
    tutor_id = models.AutoField(primary_key=True)
    document = models.ForeignKey(PersonalInformation, models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tutors'


class TutorsInterests(models.Model):
    interest = models.OneToOneField(Interests, models.DO_NOTHING, primary_key=True)
    tutor = models.ForeignKey(Tutors, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tutors_interests'
        unique_together = (('interest', 'tutor'),)


class Tutorships(models.Model):
    tutorship_id = models.AutoField(primary_key=True)
    tutorship_date = models.DateField()
    hour = models.TimeField()
    student = models.ForeignKey(Students, models.DO_NOTHING)
    tutor = models.ForeignKey(Tutors, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tutorships'


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=50)
    type = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'users'
