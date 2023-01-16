# waarmerken/admin.py

# Django
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Local
from .models import (
  Zaaktype,
  Documenttype,
  Waarmerkniveau,
  Documentwaarmerking
  )

# inline
class InLineDocumentwaarmerking(admin.StackedInline):
  model = Documentwaarmerking
  extra = 0

# Register Zaaktype
class ZaaktypeAdmin(ImportExportModelAdmin):
  fields             = ('naam', 'status',) # detailpagina (add- & editform)
  list_display       = ('naam', 'status', 'dates_created_modified',) # overzichtpagina (overschrijft "def __str__(self):" uit models.py)
  list_display_links = ('naam', 'dates_created_modified',) # create link on field(s) to detail page.
  list_editable      = ('status',) # make attributes editable in the main admin view
  list_filter        = ('naam', 'status',) # add filter on listed entities
  list_per_page      = 10 # aantal per pagina
  search_fields      = ('naam',) # add searchfield to search in listed entities
  inlines            = [InLineDocumentwaarmerking]
  # method to build combined field
  def dates_created_modified(sef, obj):
    return "{} - {}".format(obj.created, obj.modified)
 
# overall admin area
admin.site.register(Zaaktype, ZaaktypeAdmin)

# Register Documenttype
class DocumenttypeAdmin(ImportExportModelAdmin):
  list_display = ('naam',)
# overall admin area
admin.site.register(Documenttype, DocumenttypeAdmin)

# Register Waarmerkniveau
class WaarmerkniveauAdmin(admin.ModelAdmin):
  list_display = ('naam',)
# overall admin area
admin.site.register(Waarmerkniveau, WaarmerkniveauAdmin)

# inline
class InLineZaaktype(admin.StackedInline):
  model = Zaaktype

# Register Documentwaarmerking
class DocumentwaarmerkingAdmin(admin.ModelAdmin):
  #inlines = [InLineZaaktype]
  list_display = ('combi_zaak_document', 'waarmerkniveau', 'status',)
  list_editable = ('status',)
  # method to build combined field
  def combi_zaak_document(sef, obj):
    return "{} - {}".format(obj.zaaktype, obj.documenttype)

# overall admin area
admin.site.register(Documentwaarmerking, DocumentwaarmerkingAdmin)


# Register Models without layout:
#myModels = [Documentwaarmerking]  # iterable list
# overall adminarea
#admin.site.register(myModels)