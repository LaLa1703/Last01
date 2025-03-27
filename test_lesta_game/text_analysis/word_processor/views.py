from django.shortcuts import render
from .forms import UploadFileForm
from .utils import compute_tfidf

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                uploaded_file = form.save()
                with open(uploaded_file.file.path, 'r', encoding='utf-8') as file:
                    text = file.read()
                tfidf_data = compute_tfidf(text)
                return render(request, 'word_processor/tfidf_results.html', {'tfidf_data': tfidf_data})
            except Exception as e:
                error_message = f"Ошибка при обработке файла: {str(e)}"
                return render(request, 'word_processor/upload_file.html', {'form': form, 'error': error_message})
        else:
            return render(request, 'word_processor/upload_file.html', {'form': form, 'error': 'Недействительная форма. Проверьте файл и попробуйте снова.'})
    else:
        form = UploadFileForm()
    return render(request, 'word_processor/upload_file.html', {'form': form})
