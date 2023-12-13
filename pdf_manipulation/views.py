from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.conf import settings 
from .forms import UploadPDFForm
from .models import UploadedPDF
import os
# Create your views here.

def upload_pdf(request):
    form = UploadPDFForm()
    if request.method == 'POST':
        form = UploadPDFForm(request.POST, request.FILES)
        if form.is_valid():
            deal_type = form.cleaned_data['deal_type']
            # linked_client_info = form.cleaned_data['linked_client_info']
            # linked_vehicle_info = form.cleaned_data['linked_vehicle_info']
            text_boxes = None  # Placeholder, will be updated later during editing

            uploaded_pdf = UploadedPDF.objects.create(
                pdf_file=request.FILES['pdf_file'],
                deal_type=deal_type,
                # linked_client_info=linked_client_info,
                # linked_vehicle_info=linked_vehicle_info,
                text_boxes=text_boxes,
            )

            return redirect('/../edit-pdf', uploaded_pdf_id=uploaded_pdf.id)
   

    directory_path = os.path.join(settings.MEDIA_ROOT, 'uploaded_pdfs')
    file_list = os.listdir(directory_path)
    
    context = {
        'form' : form,
        'file_list' : file_list
    }
    
    return render(request, 'pdf_manipulation/upload_pdf.html', context)

# def pdf_list(request):
#     directory_path = os.path.join(settings.MEDIA_ROOT, 'uploaded_pdfs')
#     file_list = os.listdir(directory_path)
#     print(file_list)
#     return render(request, 'pdf_manipulation/upload_pdf.html', {"file_list":file_list})


def edit_pdf(request, uploaded_pdf_id):
    # Fetch the uploaded PDF object
    uploaded_pdf = get_object_or_404(UploadedPDF, id=uploaded_pdf_id)

    if request.method == 'POST':
        text_boxes_json = request.POST.get('text_boxes_json')
        uploaded_pdf.text_boxes = text_boxes_json
        uploaded_pdf.save()
        return JsonResponse({'message': 'Text boxes saved uccessfully.'})
    return render(request, 'pdf_manipulation/edit_pdf.html', {'uploaded_pdf': uploaded_pdf})