from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import StaticWeapon, Plug, PlugSet, WishlistWeapon
from api.serializers import (StaticWeaponSerializer, PlugSerializer,
  PlugSetSerializer, WishlistWeaponSerializer)

# Create your views here.
class StaticWeaponViewset(ModelViewSet):
  serializer_class = StaticWeaponSerializer
  queryset = StaticWeapon.objects.all()
  
  def get_queryset(self):
    queryset = StaticWeapon.objects.all()
    hash = self.request.query_params.get('hash')
    if hash is not None:
      queryset = queryset.filter(hash=hash)
    return queryset


class PlugViewset(ModelViewSet):
  serializer_class = PlugSerializer
  queryset = Plug.objects.all()


class PlugSetViewset(ModelViewSet):
  serializer_class = PlugSetSerializer
  queryset = PlugSet.objects.all()


class WishlistWeaponViewset(APIView):
  serializer_class = WishlistWeaponSerializer
  # queryset = WishlistWeapon.objects.all()
  
  def get_queryset(self):
    wishlist_weapons = WishlistWeapon.objects.all()
    return wishlist_weapons 

  def get(self, request, *args, **kwargs):
    try:
      hash = request.query_params['hash']
      if hash != None:
        weapon = WishlistWeapon.objects.get(hash=hash)
        serializer = WishlistWeaponSerializer(weapon)
    except:
      # wishlist_weapons = self.get_queryset()
      # serializer = WishlistWeaponSerializer(wishlist_weapons, many=True)
      return Response(False)

    return Response(serializer.data)

  def post(self, request, *args, **kwargs):
    weapon_data = request.data

    if weapon_data.get('vanguard', False):
      new_weapon = WishlistWeapon.objects.create(
        hash = weapon_data['hash'],
        name = weapon_data['name'],
        vanguard = weapon_data['vanguard'],
        crucible = None,
        gambit = None,
        junk = None
      ) 
      new_weapon.save() 
    
    elif weapon_data.get('crucible', False):
      new_weapon = WishlistWeapon.objects.create(
        hash = weapon_data['hash'],
        name = weapon_data['name'],
        vanguard = None,
        crucible = weapon_data['crucible'],
        gambit = None,
        junk = None
      ) 
      new_weapon.save() 
    
    elif weapon_data.get('gambit', False):
      new_weapon = WishlistWeapon.objects.create(
        hash = weapon_data['hash'],
        name = weapon_data['name'],
        vanguard = None,
        crucible = None,
        gambit = weapon_data['gambit'],
        junk = None
      ) 
      new_weapon.save() 

    elif weapon_data.get('junk', False):
      new_weapon = WishlistWeapon.objects.create(
        hash = weapon_data['hash'],
        name = weapon_data['name'],
        vanguard = None,
        crucible = None,
        gambit = None,
        junk = weapon_data['junk']
      ) 
      new_weapon.save() 

    serializer = WishlistWeaponSerializer(new_weapon)

    return Response(serializer.data)

  def put(self, request, *args, **kwargs):
    hash = request.query_params["hash"]
    weapon_object = WishlistWeapon.objects.get(hash=hash)
    data = request.data

    if data.get('vanguard', False):
      weapon_object.name = weapon_object.name
      weapon_object.vanguard = data['vanguard']
      weapon_object.crucible = weapon_object.crucible
      weapon_object.gambit = weapon_object.gambit
      weapon_object.junk = weapon_object.junk
      weapon_object.save()
    
    elif data.get('crucible', False):
      weapon_object.name = weapon_object.name
      weapon_object.vanguard = weapon_object.vanguard
      weapon_object.crucible = data['crucible']
      weapon_object.gambit = weapon_object.gambit
      weapon_object.junk = weapon_object.junk
      weapon_object.save()
    
    elif data.get('gambit', False):
      weapon_object.name = weapon_object.name
      weapon_object.vanguard = weapon_object.vanguard
      weapon_object.crucible = weapon_object.crucible
      weapon_object.gambit = data['gambit']
      weapon_object.junk = weapon_object.junk
      weapon_object.save()

    elif data.get('junk', False):
      weapon_object.name = weapon_object.name
      weapon_object.vanguard = weapon_object.vanguard
      weapon_object.crucible = weapon_object.crucible
      weapon_object.gambit = weapon_object.gambit
      weapon_object.junk = data['junk']
      weapon_object.save()

    serializer = WishlistWeaponSerializer(weapon_object)

    return Response(serializer.data)


def index_view(request):
  weapon = StaticWeapon.objects.get(hash=1789347249)
  column_one = weapon.column_one_hash.reusable_plug_items.all()
  plugset = PlugSet.objects.get(hash=3541408343)
  reusable_items = plugset.reusable_plug_items.all()
  weapons = StaticWeapon.objects.all().order_by('-index')
  return render(request, 'index.html', {'weapons': weapons})