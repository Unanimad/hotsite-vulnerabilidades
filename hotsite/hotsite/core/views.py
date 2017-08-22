from django.db.models import Count
from django.shortcuts import render

from hotsite.catalog.models import Vulnerability, Provider, Software


def index(request):
    template_name = 'hotsite/index.html'
    title = 'Vulnerabilidades'

    instances = Vulnerability.objects.all()

    context = {
        'title': title,
        'instances': instances
    }

    return render(request, template_name, context)


def providers(request):
    template_name = 'hotsite/providers.html'
    title = 'Fornecedores'

    instances = Provider.objects.all()
    arr_providers = []

    for instance in instances:
        # TODO: Get the product with the most vulnerabilities registered and the last update

        provider = {
            'provider': instance,
            'products': Software.objects.filter(provider=instance),
        }

        arr_providers.append(provider)

    instances = arr_providers

    context = {
        'title': title,
        'instances': instances
    }

    return render(request, template_name, context)


def provider(request, pk):
    template_name = 'hotsite/provider.html'

    instance = Provider.objects.get(pk=pk)
    instances = Software.objects.filter(provider=instance).annotate(vulnerabilities=Count('vulnerability'))

    context = {
        'head_title': instance.name,
        'title': instance.name,
        'instance': instance,
        'instances': instances
    }

    return render(request, template_name, context)


def products(request):
    template_name = 'hotsite/products.html'
    title = 'Produtos'

    instances = Software.objects.all().annotate(vulnerabilities=Count('vulnerability'))

    context = {
        'title': title,
        'instances': instances
    }

    return render(request, template_name, context)


def product(request, pk):
    template_name = 'hotsite/product.html'

    instance = Software.objects.get(pk=pk)
    instances = Vulnerability.objects.filter(products=instance)

    context = {
        'head_title': instance.name,
        'title': instance.name,
        'instances': instances,
    }

    return render(request, template_name, context)


def vulnerability(request, pk):
    template_name = 'hotsite/vulnerability.html'

    instance = Vulnerability.objects.get(pk=pk)

    context = {
        'head_title': instance.name + ' | ',
        'title': instance.name,
        'instance': instance
    }

    return render(request, template_name, context)
