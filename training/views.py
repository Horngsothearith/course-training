# Create your views here.
import datetime

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from training.serializers import *
from ulti.permission_filter import permission_filter

# region Create

# region Trainee



@api_view(['POST', ])
@permission_classes([IsAuthenticated])
def create_trainee(request):
    name = request.POST.get('name')
    name_kh = request.POST.get('name_kh')
    gender = request.POST.get('gender')
    phone = request.POST.get('phone')
    title = request.POST.get('title')
    id_number = request.POST.get('id_number')
    province = request.POST.get('province')
    operating_district = request.POST.get('operating_district')
    facility = request.POST.get('facility')

    if not name:
        return Response({'code': '400', 'error': 'name is required'}, status=status.HTTP_400_BAD_REQUEST)
    if not name_kh:
        return Response({'code': '400', 'error': 'name_kh is required'}, status=status.HTTP_400_BAD_REQUEST)
    if not gender:
        return Response({'code': '400', 'error': 'gender is required'}, status=status.HTTP_400_BAD_REQUEST)
    if not phone:
        return Response({'code': '400', 'error': 'phone is required'}, status=status.HTTP_400_BAD_REQUEST)
    if not title:
        return Response({'code': '400', 'error': 'title is required'}, status=status.HTTP_400_BAD_REQUEST)
    if not id_number:
        return Response({'code': '400', 'error': 'id_number is required'}, status=status.HTTP_400_BAD_REQUEST)
    if not province:
        return Response({'code': '400', 'error': 'province is required'}, status=status.HTTP_400_BAD_REQUEST)
    if not operating_district:
        return Response({'code': '400', 'error': 'operating_district is required'}, status=status.HTTP_400_BAD_REQUEST)
    if not facility:
        return Response({'code': '400', 'error': 'facility is required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        '''Return error'''
        Trainee.objects.get(name=name, phone=phone)
        return Response({'code': '400', 'error': 'Trainee already existed!'}, status=status.HTTP_400_BAD_REQUEST)
    except Trainee.DoesNotExist:
        '''Create if Don't have'''
        trainee = Trainee.objects.create(name=name, name_kh=name_kh, gender=gender, phone=phone, title=title,
                                         id_number=id_number, province=province, operating_district=operating_district,
                                         facility=facility)
        serializer = TraineeSerializer(trainee)
        return Response(serializer.data)


# endregion

# region Course


@api_view(['POST', ])
@permission_classes([IsAuthenticated])
def create_course(request):
    name = request.POST.get('name')
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')
    is_certification = request.POST.get('is_certification')
    certification = request.POST.get('certification')
    partner_involved = request.POST.get('partner_involved')
    province = request.POST.get('province')
    operating_district = request.POST.get('operating_district')
    facility = request.POST.get('facility')

    if not name:
        return Response({'code': '400', 'error': 'name is required'}, status=status.HTTP_400_BAD_REQUEST)
    if not start_date:
        return Response({'code': '400', 'error': 'start_date is required'}, status=status.HTTP_400_BAD_REQUEST)
    if not end_date:
        return Response({'code': '400', 'error': 'end_date is required'}, status=status.HTTP_400_BAD_REQUEST)
    if not is_certification:
        return Response({'code': '400', 'error': 'is_certification is required'}, status=status.HTTP_400_BAD_REQUEST)
    if not certification:
        return Response({'code': '400', 'error': 'certification is required'}, status=status.HTTP_400_BAD_REQUEST)
    if not partner_involved:
        return Response({'code': '400', 'error': 'partner_involved is required'}, status=status.HTTP_400_BAD_REQUEST)
    if not province:
        return Response({'code': '400', 'error': 'province is required'}, status=status.HTTP_400_BAD_REQUEST)
    if not operating_district:
        return Response({'code': '400', 'error': 'operating_district is required'}, status=status.HTTP_400_BAD_REQUEST)
    if not facility:
        return Response({'code': '400', 'error': 'facility is required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        '''Return error'''
        Course.objects.get(name=name, start_date__gte=start_date, end_date__lte=end_date)
        return Response({'code': '400', 'error': 'Course already existed!'}, status=status.HTTP_400_BAD_REQUEST)
    except Course.DoesNotExist:
        '''Create if Don't have'''
        obj = Course.objects.create(name=name, start_date=start_date, end_date=end_date,
                                    is_certification=is_certification, certification=certification,
                                    partner_involved=partner_involved,
                                    province=province,
                                    operating_district=operating_district,
                                    facility=facility)
        serializer = CourseSerializer(obj)
        return Response(serializer.data)


@api_view(['POST', ])
@permission_classes([IsAuthenticated])
def create_certification(request):
    name = request.POST.get('name')
    certification_type = request.POST.get('certification_type')
    detail = request.POST.get('detail')

    if not name:
        return Response({'code': '400', 'error': 'name is required'}, status=status.HTTP_400_BAD_REQUEST)
    if not certification_type:
        return Response({'code': '400', 'error': 'certification_type is required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        '''Return error'''
        Certification.objects.get(name=name, certification_type=certification_type)
        return Response({'code': '400', 'error': 'Certification already existed!'}, status=status.HTTP_400_BAD_REQUEST)
    except Certification.DoesNotExist:
        '''Create if Don't have'''
        obj = Certification.objects.create(name=name, certification_type=certification_type, detail=detail)
        serializer = CertificationSerializer(obj)
        return Response(serializer.data)


@api_view(['POST', ])
@permission_classes([IsAuthenticated])
def course_register(request):
    trainee = request.POST.get('trainee')
    course = request.POST.get('course')

    if not trainee:
        return Response({'code': '400', 'error': 'trainee is required'}, status=status.HTTP_400_BAD_REQUEST)
    if not course:
        return Response({'code': '400', 'error': 'course is required'}, status=status.HTTP_400_BAD_REQUEST)

    today = datetime.date.today()
    obj_trainee = Trainee.objects.get(id=trainee)
    obj_course = Course.objects.get(id=course, start_date__gte=today, end_date__lte=today)

    if not obj_course:
        return Response({'code': '400', 'error': 'Course has already closed!'},
                        status=status.HTTP_400_BAD_REQUEST)
    try:
        '''Return error'''
        CourseRegistration.objects.get(trainee=trainee, course=course)
        return Response({'code': '400', 'error': 'Trainee has already registered to this course!'},
                        status=status.HTTP_400_BAD_REQUEST)
    except CourseRegistration.DoesNotExist:
        '''Create if Don't have'''
        obj = CourseRegistration.objects.create(trainee=trainee, course=course,
                                                province=obj_trainee.province,
                                                operating_district=obj_trainee.operating_district,
                                                facility=obj_trainee.facility)
        serializer = CourseRegistrationSerializer(obj)
        return Response(serializer.data)


@api_view(['POST', ])
@permission_classes([IsAuthenticated])
def create_attendance(request):
    trainee = request.POST.get('trainee')
    course = request.POST.get('course')

    if not trainee:
        return Response({'code': '400', 'error': 'trainee is required'}, status=status.HTTP_400_BAD_REQUEST)
    if not course:
        return Response({'code': '400', 'error': 'course is required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        '''Return error'''
        Attendance.objects.get(check_date__day=datetime.date.today().day, check_date__month=datetime.date.today().month,
                               check_date__year=datetime.date.today().year, trainee=trainee, course=course)
        return Response({'code': '400', 'error': 'Trainee has already checked in!'}, status=status.HTTP_400_BAD_REQUEST)
    except Attendance.DoesNotExist:
        '''Create if Don't have'''
        obj = Attendance.objects.create(trainee=trainee, course=course)
        serializer = AttendanceSerializer(obj)
        return Response(serializer.data)


# endregion

# endregion

# region Get

# region all data
@api_view(['GET', ])
@permission_classes([IsAuthenticated])
def get_all_trainee(request):
    user = request.user
    obj = Trainee.objects.all()
    obj = permission_filter(user, obj)

    serializer = TraineeSerializer(obj, many=True)
    return Response(serializer.data)


@api_view(['GET', ])
@permission_classes([IsAuthenticated])
def get_all_course(request):
    user = request.user
    obj = Course.objects.all()
    obj = permission_filter(user, obj)

    serializer = CourseSerializer(obj, many=True)
    return Response(serializer.data)


@api_view(['GET', ])
@permission_classes([IsAuthenticated])
def get_all_course_register(request):
    user = request.user
    obj = CourseRegistration.objects.all()
    obj = permission_filter(user, obj)

    serializer = CourseRegistrationSerializer(obj, many=True)
    return Response(serializer.data)


@api_view(['GET', ])
@permission_classes([IsAuthenticated])
def get_all_certification(request):
    obj = Certification.objects.all()

    serializer = CertificationSerializer(obj, many=True)
    return Response(serializer.data)


@api_view(['GET', ])
@permission_classes([IsAuthenticated])
def get_all_attendance(request):
    obj = Attendance.objects.all()

    serializer = AttendanceSerializer(obj, many=True)
    return Response(serializer.data)

# endregion

# region by id
@api_view(['GET', ])
@permission_classes([IsAuthenticated])
def get_trainee_by_id(request):
    trainee_id = request.POST.get('id')
    user = request.user
    try:
        obj = Trainee.objects.filter(id=trainee_id)
    except Trainee.DoesNotExist:
        return Response({'code': '400', 'error': 'Trainee does not exist!'}, status=status.HTTP_400_BAD_REQUEST)

    obj = permission_filter(user, obj)
    if not obj:
        return Response({'code': '400', 'error': 'You do not have permission.'}, status=status.HTTP_400_BAD_REQUEST)
    serializer = TraineeSerializer(obj, many=True)
    return Response(serializer.data)


@api_view(['GET', ])
@permission_classes([IsAuthenticated])
def get_course_by_id(request):
    course_id = request.POST.get('id')
    user = request.user
    try:
        obj = Course.objects.filter(id=course_id)
    except Course.DoesNotExist:
        return Response({'code': '400', 'error': 'Course does not exist!'}, status=status.HTTP_400_BAD_REQUEST)

    obj = permission_filter(user, obj)
    if not obj:
        return Response({'code': '400', 'error': 'You do not have permission.'}, status=status.HTTP_400_BAD_REQUEST)
    serializer = CourseSerializer(obj, many=True)
    return Response(serializer.data)


@api_view(['GET', ])
@permission_classes([IsAuthenticated])
def get_certification_by_id(request):
    cert_id = request.POST.get('id')
    try:
        obj = Certification.objects.filter(id=cert_id)
    except Certification.DoesNotExist:
        return Response({'code': '400', 'error': 'Certification does not exist!'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = CertificationSerializer(obj, many=True)
    return Response(serializer.data)


# endregion

# endregion
