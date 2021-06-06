# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from master_data.serializers import *

# region Create

# region Province
from ulti.permission_filter import permission_filter


@api_view(['POST', ])
@permission_classes([IsAuthenticated])
def create_province(request):
    province = request.POST.get('province')
    description = request.POST.get('description')
    if not province:
        return Response({'code': '400', 'error': 'province is required'}, status=status.HTTP_400_BAD_REQUEST)
    if not description:
        return Response({'code': '400', 'error': 'description is required'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        '''Return error'''
        Province.objects.get(province=province)
        return Response({'code': '400', 'error': 'Province already existed!'}, status=status.HTTP_400_BAD_REQUEST)
    except Province.DoesNotExist:
        '''Create if Don't have'''
        prov = Province.objects.create(province=province, description=description)
        serializer = ProvinceSerializer(prov)
        return Response(serializer.data)


@api_view(['POST', ])
@permission_classes([IsAuthenticated])
def create_province_kh(request):
    province = request.POST.get('province')
    description = request.POST.get('description')
    if not province:
        return Response({'code': '400', 'error': 'province is required'}, status=status.HTTP_400_BAD_REQUEST)
    if not description:
        return Response({'code': '400', 'error': 'description is required'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        '''Return error'''
        ProvinceKh.objects.get(province=province)
        return Response({'code': '400', 'error': 'Province already existed!'}, status=status.HTTP_400_BAD_REQUEST)
    except ProvinceKh.DoesNotExist:
        '''Create if Don't have'''
        prov = ProvinceKh.objects.create(province=province, description=description)
        serializer = ProvinceKhSerializer(prov)
        return Response(serializer.data)


# endregion

# region Operating District
@api_view(['POST', ])
@permission_classes([IsAuthenticated])
def create_operating_district(request):
    od = request.POST.get('operating_district')
    description = request.POST.get('description')
    if not od:
        return Response({'code': '400', 'error': 'operating_district is required'}, status=status.HTTP_400_BAD_REQUEST)
    if not description:
        return Response({'code': '400', 'error': 'description is required'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        '''Return error'''
        OperatingDistrict.objects.get(operating_district=od)
        return Response({'code': '400', 'error': 'Operating District already existed!'},
                        status=status.HTTP_400_BAD_REQUEST)
    except OperatingDistrict.DoesNotExist:
        '''Create if Don't have'''
        opd = OperatingDistrict.objects.create(operating_district=od, description=description)
        serializer = OperatingDistrictSerializer(opd)
        return Response(serializer.data)


@api_view(['POST', ])
@permission_classes([IsAuthenticated])
def create_operating_district_kh(request):
    od = request.POST.get('operating_district')
    description = request.POST.get('description')
    if not od:
        return Response({'code': '400', 'error': 'operating_district is required'}, status=status.HTTP_400_BAD_REQUEST)
    if not description:
        return Response({'code': '400', 'error': 'description is required'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        '''Return error'''
        OperatingDistrictKh.objects.get(operating_district=od)
        return Response({'code': '400', 'error': 'Operating District already existed!'},
                        status=status.HTTP_400_BAD_REQUEST)
    except OperatingDistrictKh.DoesNotExist:
        '''Create if Don't have'''
        opd = OperatingDistrictKh.objects.create(operating_district=od, description=description)
        serializer = OperatingDistrictKhSerializer(opd)
        return Response(serializer.data)


# endregion

# region Facility
@api_view(['POST', ])
@permission_classes([IsAuthenticated])
def create_facility_type(request):
    f_name = request.POST.get('name')
    if not f_name:
        return Response({'code': '400', 'error': 'name is required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        '''Return error'''
        FacilityType.objects.get(name=f_name)
        return Response({'code': '400', 'error': 'Facility already existed!'},
                        status=status.HTTP_400_BAD_REQUEST)
    except FacilityType.DoesNotExist:
        '''Create if Don't have'''
        fac_type = FacilityType.objects.create(name=f_name)
        serializer = FacilityTypeSerializer(fac_type)
        return Response(serializer.data)


@api_view(['POST', ])
@permission_classes([IsAuthenticated])
def create_facility(request):
    f = request.POST.get('facility')
    f_name = request.POST.get('name')
    f_type = request.POST.get('type')
    f_status = request.POST.get('status')

    if not f:
        return Response({'code': '400', 'error': 'facility is required'}, status=status.HTTP_400_BAD_REQUEST)
    if not f_name:
        return Response({'code': '400', 'error': 'name is required'}, status=status.HTTP_400_BAD_REQUEST)
    if not f_type:
        return Response({'code': '400', 'error': 'type is required'}, status=status.HTTP_400_BAD_REQUEST)
    if not f_status:
        return Response({'code': '400', 'error': 'status is required'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        '''Return error'''
        Facility.objects.get(facility=f, name=f_name)
        return Response({'code': '400', 'error': 'Facility already existed!'},
                        status=status.HTTP_400_BAD_REQUEST)
    except Facility.DoesNotExist:
        '''Create if Don't have'''
        facility = Facility.objects.create(facility=f, name=f_name, type=f_type, status=f_status)
        serializer = FacilitySerializer(facility)
        return Response(serializer.data)


@api_view(['POST', ])
@permission_classes([IsAuthenticated])
def create_facility_kh(request):
    facility = request.POST.get('facility')
    f_name = request.POST.get('name')
    f_type = request.POST.get('type')
    f_status = request.POST.get('status')
    if not f_name:
        return Response({'code': '400', 'error': 'name is required'}, status=status.HTTP_400_BAD_REQUEST)
    if not f_type:
        return Response({'code': '400', 'error': 'type is required'}, status=status.HTTP_400_BAD_REQUEST)
    if not f_status:
        return Response({'code': '400', 'error': 'status is required'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        '''Return error'''
        FacilityKh.objects.get(name=f_name)
        return Response({'code': '400', 'error': 'Facility already existed!'},
                        status=status.HTTP_400_BAD_REQUEST)
    except FacilityKh.DoesNotExist:
        '''Create if Don't have'''
        fac = FacilityKh.objects.create(facility=facility, name=f_name, type=f_type, status=f_status)
        serializer = FacilityKhSerializer(fac)
        return Response(serializer.data)


# endregion

# endregion

# region Get
# region all
@api_view(['GET', ])
@permission_classes([IsAuthenticated])
def get_all_province(request):
    user = request.user
    obj = Province.objects.all()
    obj = permission_filter(user, obj)

    serializer = ProvinceSerializer(obj, many=True)
    return Response(serializer.data)


@api_view(['GET', ])
@permission_classes([IsAuthenticated])
def get_all_operating_district(request):
    user = request.user
    obj = OperatingDistrict.objects.all()
    obj = permission_filter(user, obj)

    serializer = OperatingDistrictSerializer(obj, many=True)
    return Response(serializer.data)


@api_view(['GET', ])
@permission_classes([IsAuthenticated])
def get_all_facility(request):
    user = request.user
    obj = Facility.objects.all()
    obj = permission_filter(user, obj)

    serializer = FacilitySerializer(obj, many=True)
    return Response(serializer.data)


@api_view(['GET', ])
@permission_classes([IsAuthenticated])
def get_operating_district_by_province(request):
    province = request.GET.get('province')
    user = request.user
    obj = OperatingDistrict.objects.filter(operating_district__startswith=province)
    obj = permission_filter(user, obj)

    serializer = OperatingDistrictSerializer(obj, many=True)
    return Response(serializer.data)


@api_view(['GET', ])
@permission_classes([IsAuthenticated])
def get_facility_by_operating_district(request):
    od = request.GET.get('od')
    user = request.user
    obj = Facility.objects.filter(facility__startswith=od)
    obj = permission_filter(user, obj)

    serializer = FacilitySerializer(obj, many=True)
    return Response(serializer.data)
# endregion
# endregion
