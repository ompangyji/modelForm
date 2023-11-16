from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.

def index(request):
    articles = Article.objects.all()

    context = {
        'articles': articles
    }

    return render(request, 'index.html', context)

def create(request):
    # 모든 경우의수
    # 1. GET : form을 만들어서 html 문서를 사용자에게 리턴
    #           => 1~4
    # 2. POST invalid data (데이터 검증에 실패하는경우)
    #  => 검증에 성공한 데이터만 가지고 form을 만들어서 html 문서를 사용자에게 리턴
    #          => 5~9
    # 3. POST valid data (데이터 검증에 성공하는경우)
    #  => DB에 데이터 저장후 index페이지로 redirect

    # ==========
    # 5. POST요청 (데이터가 잘못들어온 경우)
    # 10. POST요청 (데이터가 잘들어온 경우)

    if request.method == 'POST':
        # 6. 사용자가 입력한 정보(X)를 담아서 form을 생성
        # 11. 사용자가 입력한 정보(O)를 담아서 form을 생성
        form = ArticleForm(request.POST)

        # 7. form을 검증 (실패)
        # 12. form을 검증 (성공)
        if form.is_valid():
            article = form.save()
            # 13. form을 저장
            return redirect('articles:index')
            # 14. index페이지로 redirect
    # 1. GET 요청
    else:
        # 2. 비어있는 form을 만들어서
        form = ArticleForm()

    # 3. context dict에 담고
    # 8. 검증에 실패한 form을 context dict에 담고
    context = {
        'form': form,
    }

    # 4. create.html을 랜더링
    # 9. create.html을 랜더링
    return render(request, 'create.html', context)

def delete(request, id):
    article = Article.objects.get(id=id)
    article.delete()

    return redirect('articles:index')