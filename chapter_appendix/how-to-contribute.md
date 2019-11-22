<!--
# How to Contribute to This Book
:label:`chapter_contribute`
-->

# Cách đóng góp vào dự án dịch sách này
:label:`chapter_contribute`

_Trang này được thay đổi một chút để phù hợp với dự án dịch sách ra tiêngs Việt_

<!--
Contributions by [readers](https://github.com/d2l-ai/d2l-en/graphs/contributors) help us improve this book. If you find a typo, an outdated link, something where you think we missed a citation, where the code doesn't look elegant or where an explanation is unclear, please contribute back and help us help our readers. While in regular books the delay between print runs (and thus between typo corrections) can be measured in years, it typically takes hours to days to incorporate an improvement in this book. This is all possible due to version control and continuous integration testing. To do so you need to install Git and submit a [pull request](https://github.com/d2l-ai/d2l-en/pulls) to the GitHub repository. When your pull request is merged into the code repository by the author, you will become a contributor. In a nutshell the process works as described in the diagram below.
-->

Những đóng góp từ [độc giả](https://github.com/d2l-ai/d2l-en/graphs/contributors) giúp chúng tôi
cải thiện cuốn sách này. Nếu bạn tìm thấy một lỗi chính tả, một đường dẫn đã hết hạn, một điểm mà
bạn cho trằng chúng tôi thiếu trích dẫn, một đoạn mã chưa hợp lý hoặc một lời giải thích chưa rõ
ràng, vui lòng đóng góp bản sửa đổi để giúp các độc giả khác. Trong với khi những cuốn sách thông
thường, thời gian giữa hai bản in có thể được đo bằng năm (và giữa hai bản sửa lỗi chính tả cũng
vậy), thường chỉ mất vài giờ tới vài ngày để tạo một sự thay đổi trong cuốn sách này. Việc này được
thực hiện nhờ vào các công cụ quản lý phiên bản và các bài kiểm tra tự động tích hợp liên tục. Để
làm được việ này, bạn cần cài đặt Git và nộp một [pull request](https://github.com/aivivn/d2l-vn/pulls)
vào trang chủ GitHub của dự án này. Khi pull request của bạn được chấp nhận và hợp nhất với bản chính,
bạn trở thành một cộng tác viên. Quy trình này được mô tả như sơ đồ dưới đây:

<!--
![Contributing to the book.](../img/contribute.svg)
-->

![Đóng góp vào dự án dịch sách](../img/contribute.svg)

<!--
## From Reader to Contributor in 6 Steps
-->

## Sáu bước từ độc giả tới cộng tác viên

<!--
We will walk you through the steps in detail. If you are already familiar with Git you can skip this section. For concreteness we assume that the contributor's user name is `smolix`.
-->

Chúng tôi sẽ hướng dẫn bạn chi tiết từng bước. Nếu bạn đã quen với Git bạn có thể bỏ qua phần này.
Giả sử thằng tên của cộng tác viên là `smolix`.

<!--
### Install Git
-->

### Cài đặt Git

<!--
The Git open source book describes [how to install Git](https://git-scm.com/book/zh/v2). This typically works via `apt install git` on Ubuntu Linux, by installing the Xcode developer tools on macOS, or by using GitHub's [desktop client](https://desktop.github.com). If you don't have a GitHub account, you need to sign up for one [4].
-->

Cuốn sách mã nguồn mở về Git mô tả [cách cài đặt Git](https://git-scm.com/book/zh/v2). Việc này
thường được thực hiên bằng `apt install git` trên Ubuntu Linux, bằng cài đặt công cụ phát triên Xcode
trên macOS, hoặc bằng sử dụng [GitHub cho máy tính](https://détop.github.com). Nếu bạn chưa có
tài khoản GitHub, bạn có thể đăng ký như hướng dẫn trong [4].

<!--
### Log in to GitHub
-->

### Đăng nhập vào GitHub

<!--
Enter the [address](https://github.com/d2l-ai/d2l-en/) of the book's code repository in your browser. Click on the `Fork` button in the red box at the top-right of the figure below, to make a copy of the repository of this book. This is now *your copy* and you can change it any way you want.
-->

Nhập [địa chỉ](https://github.com/aivivn/d2l-vn) của cuốn sách này trên trình duyệt. Click và nút
`Fork` trong khung màu đỏ phía trên bên phải của hình dưới đây để tạo một bản copy của dự án dịch
sách này. Bây giờ bạn đã có một bản sao của mình và có thể sửa đổi bất cứ điều gì bạn muốn.

<!-- TODO: changet the figure -->
![The code repository page.](../img/git-fork.png)
:width:`700px`

<!--
Now, the code repository of this book will be copied to your username, such as `smolix/d2l-en` shown at the top-left of the screenshot below.
-->

Bây giờ, trang dự án của cuốn sách này được sao chép với tên tài khoản của bạn, chẳng hạn `smolix/d2l-vn`
như được hiển thị ở góc trên bên trái của ảnh dưới đây.

![Copy the code repository.](../img/git-forked.png)
:width:`700px`

<!--
### Clone the Repository
-->

### Tải dự án về máy

<!--
To clone the repository (i.e. to make a local copy) we need to get its repository address. The green button on the picture below displays this. Make sure that your local copy is up to date with the main repository if you decide to keep this fork around for longer. For now simply follow the instructions in :numref:`chapter_installation` to get started. The main difference is that you're now downloading *your own fork* of the repository.
-->

Để tải dự án này xuống máy chúng ta cần đường dẫn của nói bằng cách click vào nút màu xanh lục như trong ảnh dưới đây.
Đảm bảo rằng bản copy trên máy của bạn luôn được cập nhật với bản trên trang chủ dự án dịch nếu bạn
có ý định giữ lại bản này trong máy và đóng góp nhiêù hơn. Để bắt đầu, bạn có thể làm theo hướng dẫn
tại :numref:`chapter_installation`. Sự khác biệt là bạn bây giờ tải về dự án trên chính trang của bạn thay vì
từ trang chủ của dự án dịch.

<!--
![Git clone.](../img/git-clone.png)
:width:`700px`
-->

```
# Replace your_github_username with your GitHub username
git clone https://github.com/your_github_username/d2l-vn.git
```

<!--
On Unix the above command copies all the code from GitHub to the directory `d2l-en`.
-->

Trong Unix, câu lệnh trên đây copy tất cả mã nguồn từ GitHub về thư mục `d2l-en`.

<!--
### Edit the Book and Push
-->

### Sửa đổi theo ý bạn và đẩy lên

<!--
Now it's time to edit the book. It's best to edit the notebooks in Jupyter following instructions in :numref:`chapter_jupyter`. Make the changes and check that they're OK. Assume we have modified a typo in the file `~/d2l-en/chapter_appendix/how-to-contribute.md`.
You can then check which files you have changed:
-->

Bây giờ đến lúc sửa đổi cuốn sách. Giả sử bạn sử một lỗi chính tả trong tập tin `~/d2l-vn/chapter_appendix/hơ-to-contribute.md`.
Sau khi sửa xong, bạn có thể kiểm tra những tập tin nào đã được thay đổi:

```
git status
```

<!--
At this point Git will prompt that the `chapter_appendix/how-to-contribute.md` file has been modified.
-->

Tới thời điêmr này Git sẽ hiển thị tập tin `chapter_appendix/how-to-contribute.md` đã bị sửa đổi.

```
mylaptop:d2l-en smola$ git status
On branch master
Your branch is up-to-date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   chapter_appendix/how-to-contribute.md
```

<!--
After confirming that this is what you want, execute the following command:
-->

Sau khi xác nhận rằng việc thay đổi đúng với ý đồ của bạn, thực thi câu lệnh dưới đây:

```
git add chapter_appendix/how-to-contribute.md
git commit -m 'fix typo in git documentation'
git push
```

<!--
The changed code will then be in your personal fork of the repository. To request the addition of your change, you have to create a pull request for the official repository of the book.
-->

Đoạn mã bị thay đổi sau đó sẽ được cập nhật trên trang dự án của bạn. Để yêu cầu sửa đổi trên trang chủ dự án,
bạn phải tạo một pull request.

<!--
### Pull Request
-->

### Pull Request

<!--
Go to your fork of the repository on GitHub and select "New pull request". This will open up a screen that shows you the changes between your edits and what is current in the main repository of the book.
-->

Mở trang dự án của bạn trên GitHub và chọn "New pull request". Một màn hình sẽ hiện ra chỉ cho bạn
sự thay đổi giữa bản sửa đổi của bạn và bản gốc hiện thời trên trang chủa dự án dịch sách.
![Pull Request.](../img/git-newpr.png)
:width:`700px`


<!--
### Submit Pull Request
-->

### Nộp Pull Request

<!--
Finally, submit a pull request. Make sure to describe the changes you have made in the pull request. This will make it easier for the authors to review it and to merge it with the book. Depending on the changes, this might get accepted right away, rejected, or more likely, you'll get some feedback on the changes. Once you've incorporated them, you're good to go.
-->

Cuối cùng, bạn cần nộp một pull request. Nhớ mô tả những thay đổi của bạn trong pull request này.
Việc này giúp nhóm điều hành và các cộng tác viên khác dễ dàng phản biện và hợp nhất pull request của
bạn vào bản gốc. Tuỳ thuộc và sự sửa đổi, việc này có thể được chấp nhật tức thì, bị từ chối, hoặc phổ biến
hơn, bạn sẽ nhận được phản hồi. Một khi bạn sửa đổi theo tất cả phản hồi, pull request sẽ được hợp vào bản gốc.

<!--
![Create Pull Request.](../img/git-createpr.png)
:width:`700px`
-->
![Tạo Pull Request.](../img/git-createpr.png)
:width:`700px`

<!--
Your pull request will appear among the list of requests in the main repository. We will make every effort to process it quickly.
-->

Pull request của bạn sẽ xuất hiện trong danh sách các pull request trong dự án chính. Chúng tôi sẽ cố gắng để xử lý pull request của bạn một cách nhanh chóng.

<!--
## Summary
-->

## Tóm tắt

<!--
* You can use GitHub to contribute to this book.
* Forking a repositoy is the first step to contributing, since it allows you to edit things locally and only contribute back once you're ready.
* Pull requests are how contributions are being bundled up. Try not to submit huge pull requests since this makes them hard to understand and incorporate. Better send several smaller ones.
-->

* Bạn có thể sử dụng GitHub để đóng góp vào dự án dịch.
* Tạo bản sao về tài khoản của bạn là bước đầu tiên để đóng góp, vì nó cho phép bạn sửa đổi theo ý mình và đóng góp khi đã sẵn sàng.
* Pull request là cách những đóng góp được gộp lại với nhau. Cố gắng tránh nộp những pull request quá lớn vì việc này khiến việc kiểm tra,
phản hồa và tích hợp trở nên khó khăn. Tốt hơn hết là nộp những pull request nhỏ, mỗi pull request thực hiện một tác vụ nhỏ.

<!--
## Exercises
-->

## Bài tập

<!--
1. Star and fork the `d2l-en` repository.
1. Find some code that needs improvement and submit a pull request.
1. Find a reference that we missed and submit a pull request.
-->

1. Click vào nút 'Star' rồi 'Fork' dự án `d2l-vn`.
2. Tìm những chỗ cần dịch hoặc sửa đổi sau đó nộp một pull request

<!--
## Scan the QR Code to [Discuss](https://discuss.mxnet.io/t/2401)
-->
## Quét mã QR để [Thảo luận](https://discuss.mxnet.io/t/2401)

![](../img/qr_how-to-contribute.svg)
