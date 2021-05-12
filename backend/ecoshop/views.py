from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ecoshop.models import Shop
from ecoshop.serializers import ShopSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def ecoshop_list(request):
    data = request.data["location"]

    addr1 = address_finder(data['1'], data['2'])
    addr2 = address_finder(data['3'], data['4'])
    address = address_finder(addr1, addr2)

    queryset = Shop.objects.filter(address__startswith=address)
    serializer = ShopSerializer(queryset, many=True)

    return Response(serializer.data)


def address_finder(addr1, addr2):
    result = ""
    len1, len2 = len(addr1), len(addr2)
    for i in range(len1):
        match = ""
        for j in range(len2):
            if i + j < len1 and addr1[i + j] == addr2[j]:
                match += addr2[j]
            else:
                if len(match) > len(result):
                    result = match
                match = ""
    return result
