from django.http import JsonResponse

from setting_uom.models import GroupUomDefinition, Uom


def get_uom(request):
    if request.method == "GET":
        group_id = request.GET.get("group_id", None)
        group_uom_definition = GroupUomDefinition.objects.get(group_id=group_id)
        try:
            uom = Uom.objects.filter(id__in=[group_uom_definition.uom_to.id, group_uom_definition.base_uom.id])
        except Exception:
            data = {'error_message': 'error'}
            return JsonResponse(data)
        return JsonResponse(list(uom.values('id', 'uom_name')), safe=False)