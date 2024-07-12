from django.shortcuts import render, redirect, get_object_or_404
from sample_app.models import Post
from django.forms import ModelForm


def create_post(request):
    """
    新たなデータを作成する
    """
    # オブジェクトを新規作成する
    post = Post()

    # ページロード時
    if request.method == 'GET':
        # 新規作成オブジェクトにより form を作成
        form = PostForm(instance=post)

        # ページロード時は form を Template に渡す
        return render(request,
                      'sample_app/post_form.html',  # 呼び出す Template
                      {'form': form})  # Template に渡すデータ

    # 実行ボタン押下時
    if request.method == 'POST':
        # POST されたデータにより form を作成
        form = PostForm(request.POST, instance=post)

        # 入力されたデータのバリデーション
        if form.is_valid():
            # チェック結果に問題なければデータを作成する
            post = form.save(commit=False)
            post.save()

        return redirect('sample_app:read_post')


def edit_post(request, post_id):
    """
    対象のデータを編集する
    """
    # IDを引数に、対象オブジェクトを取得
    post = get_object_or_404(Post, pk=post_id)

    # ページロード時
    if request.method == 'GET':
        # 対象オブジェクトにより form を作成
        form = PostForm(instance=post)

        # ページロード時は form とデータIDを Template に渡す
        return render(request,
                      'sample_app/post_form.html',  # 呼び出す Template
                      {'form': form, 'post_id': post_id})  # Template に渡すデータ

    # 実行ボタン押下時
    elif request.method == 'POST':
        # POST されたデータにより form を作成
        form = PostForm(request.POST, instance=post)

        # 入力されたデータのバリデーション
        if form.is_valid():
            # チェック結果に問題なければデータを更新する
            post = form.save(commit=False)
            post.save()

        # 実行ボタン押下時は処理実行後、一覧画面にリダイレクトする
        return redirect('sample_app:read_post')


def read_post(request):
    """
    データ一覧を表示する
    """
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'sample_app/post_list.html', {'posts': posts})


def delete_post(request, post_id):
    # 対象のオブジェクトを取得
    post = get_object_or_404(Post, pk=post_id)
    post.delete()

    # 削除リクエスト時は削除実行後、一覧表示画面へリダイレクトする
    return redirect('sample_app:read_post')


class PostForm(ModelForm):
    """
    フォーム定義
    """
    class Meta:
        model = Post
        # fields は models.py で定義している変数名
        fields = ('title', 'content')
