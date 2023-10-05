# Шпаргалка по работе с GIT от Яндекса в моей редакции<br>
## Командная строка<br>
<br>
**pwd** - от англ. _print working directory_ - "Показать рабочую папку". Выводит путь к текущей директории.<br>
**cd** - от англ. _change directory_ - "Сменить директорию". Команда для перехода между директориями. **~** - обозначение домашней директории. Если путь к директории содержит пробелы, его нужно заключать в кавычки. **.** - текущая директория. **..** - родительская директория.<br>
**ls** - от англ. _list directory contents_ - "Отобразить содержимое директории". **ls -s** - выводит расширенный список. В нем отобразятся все скрытые файлы, которые начинаются с ".".<br>
**touch** - команда для создания файла, с именем файла в качестве параметра<br>
**mkdir** - от англ. _makr directory_ - "Создать директорию". Можно создать целую структуру директорий одной командой с помощью фалга **-p**.<br>
**mkdir -p dir1/dir2/dir3** - создает несколько директорий, вложенных друг в друга.<br>
**cp** - от англ. _copy_ - "Копировать". Команда для копирования файлов. В качестве параметров указывается что копируется и куда копируется. Можно указать сразу несколько файлов.<br>
**mv** - от англ. _move_ - "Переместить". После имени команды указывают список файлов и папок, которые нужно переместить, а затем - папку, в которую нужно выполнить перемещение.<br>
**cat** - от англ. _concatenate and print_ - "Объединить и распечатать". Команда прочитает файл в консоль. Команда работает только с текстовыми файлами.<br>
**rm** - от англ. _remove_ - "Удалить". Команда удаляет файл. Флаг **-r** - от англ. _recursive_ - "Рекурсивный" позволяет удалять папку с файлами<br>
**rmdir** от англ. _remove directory_ - "Удалить директорию". Команда удаляет директорию, но она должна быть пустой.<br>
<br>
Команды в терминале можно указывать не по одной, а сразу списком. Для этого их нужно разделить двумя амперсандами **&&**.<br>
<br>
Если нужно найти написать какую-либо команду, достаточно вспомнить, с каких букв она начинается и дважды нажать **Tab**. **Tab** не только дописывает команды, но и пути.<br>

---

## Команды Git<br>
<br>
**git version** - консоль выдает текущую версию установленного Git<br>
**git config --global user.name "User Ivanov"**<br>
**git config --global user.email user@yandex.ru**<br>
В настройках Git указываем свое имя (латиницей) и свой электронный почтовый ящик.<br>
Все глобальные настройки Git хранит в файле **.gitconfig** в домашней директории.<br>
**git config --list** - вывести содержимое файла Git<br>
**git init** - сделать текущую папку репозиторием. В текущей директории создается директория ".git", в которой будет хранится служебная информация. <br>
"Разгитить" папку можно удалением этой директории. В консоли выполнить команду **rm -rf .git**. **f** отключит запросы на подтверждения удаления файлов.<br>
**git status** - показать текущее состояние репозитория<br>
**git add** - подготавливает файлы к сохранению в репозитории. После этой команды необходимо указать файл (файлы). Ключ **--all** позволяет подготовить к сохранению все файлы.<br>
**git commit -m 'Коментарий к коммиту' - Сделать коммит с ключем -m, который присваивает коммиту сообщение. Сообщение пишется в кавычках.<br>
**git log** - выводит коммиты в обратном хронологическом порядке.<br>
**git log --online** - сокращенный лог.
<br>
Для генерации SSH-пары ключей используется программа **ssh-keygen**.<br>
**ssh-keygen -t ed25519 -C "электронная почта, к которой привязан ваш аккаунт на GitHud"<br>
В случае возникновения ошибки необходимо использовать другой алгоритм шифрования.<br>
**ssh-keygen -t rsa -b 4096 -C "электронная почта, к которой привязан ваш аккаунт на GitHud"<br>
**clip < ~/.ssh/id_rsa.pub** или **clip < ~/.ssh/id_ed25519.pub** - копирование содержимого ключа из консоли в буфер обмена.<br>
**ssh -T git@github.com** - проверить правильность ключа.<br>
<br>
Для того, чтобы привязать удаленный репозиторий к локальному необходимо перейти в директорию репозитория и выполнить команду:<br>
**git remote add origin git@github.com:%имя_аккаунта%/%имя_проекта%.git<br>
Команде необходимо передать два параметра: имя удаленного репозитория и его URL. В качестве имени используйте имя origin, а URL скопировать со страницы удаленного репозитория.<br>
**git remote -v** - убедится, что локальный репозиторий связан с удаленным. В выводе должны быть две строчки.<br>
**git push** - загрузить содержимое локального репозитория на GitHub. Первый раз эту команду нужно вызвать с флагом **-u** и параметром **origin** и **main** или **master**. Флаг **-u** свяжет локальную ветку с одноименной удаленной.<br>

---

HEAD -- это голова.
Коммит -- это всему голова.
Статусы файлов:
<br>
<br>
'''
<br>
mermaid
<br>
graph LR;
<br>
untracked -- "git add" --> staged;
<br>
staged -- "???" --> tracked/comitted;
<br>
%% стрелка без текста для примера:
<br>
A --> B;
<br>
%% описание схемы
<br>
'''
<br>
<br>


git commit --amend - исправить созданный коммит. Работает только с последним коммитом<br>
git commit --amend --no-edit после добавления дополнительных файлов делаем коммит с данными параметрами. коментарии не поменяются.<br>
git commit --amend -m 'Новое сообщение' Если добавлять новые файлы не нужно, а изменить комментарий к последнему коммиту необходимо.<br>