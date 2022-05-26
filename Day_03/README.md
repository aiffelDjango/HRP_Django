# Day_03 Summary; Django Setting and CSS

- 진행 날짜: 22.04.20
- [작성 참고 1](https://github.com/aiffelDjango/KUD/blob/main/README/CSS/3.CSS.md)
- [작성 참고 2](https://github.com/aiffelDjango/KUD/blob/main/README/CSS/3-2.CSS.md)

## 결과 화면

![CSS Project Image](https://github.com/aiffelDjango/KUD/raw/main/README/CSS/img/CSS1.png)

## CSS Project

### HTML

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel = "stylesheet" href = "../../static/CSS/main.css">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poiret+One&display=swap');
    </style>
    <title>PortFolio</title>
</head>
<body>

    <!-- 전체 감싸는 태그 -->
    <div id="container">
        <!-- 네비게이션 태그  -->
        <nav>
            <ul>
                <li><a href = "#Home"><b>Home</b></a></li>
                <li><a href = "#About"><b>About</b></a></li>
                <li><a href = "#Gallery"><b>Gallery</b></a></li>
                <li><a href = "#Contact"><b>Contact</b></a></li>
            </ul>
        </nav>

        <!-- 컨텐츠 시작  -->

        <!-- 첫번째 페이지  -->
        <div id="Home" class="listItem">
            <h1> Home </h1>
            <span class="profile">
                <!-- 이미지 크기 550X550px -->
                <img src=" ../../static/imgs/main.jpg" width="550px;" height="550px" alt=""/>
            </span>
            <h3>
                <strong>This Cat is so Cute</strong>
                <br>You can scroll down if you want to see me more!
            </h3>
        </div>

        <!-- 두번째 페이지  -->
           <div id="About" class="listItem">
            <h1> About </h1>
            <div>
            <!-- 이미지 크기 300X300px -->
               <img class = "profile" src ="../../static/imgs/two.jpg" alt="" width="300px" height="300px">
                <div class="AboutContents">
                    <h2>
                        <strong>Lorem ipsum dolor sit amet <br>Lorem ipsum dolors</strong>
                    </h2>
                    <h3 class ="intext">
                        Lorem ipsum dolor sit amet consectetur adipisicing elit.<br>
                        Repudiandae a tempora quis soluta, ratione architecto!<br>
                        Facere, possimus modi ducimus perspiciatis nostrum<br>
                        dolorum id voluptatum fuga totam sint harum. Quae, nemo!<br>
                        Repudiandae a tempora quis soluta, ratione architecto!<br>
                        Facere, possimus modi ducimus perspiciatis nostrum<br>
                        dolorum id voluptatum fuga totam sint harum. Quae, nemo!<br>
                    </h3>
                </div>
             </div>
        </div>
        <!-- 세번째 페이지  -->
        <div id="Gallery" class="listItem">
            <h1> Gallery  </h1>
            <div class = "favorites">
                <div class="GalleryItems">
                    <img class = "grid_item" src="../../static/imgs/3-1.jpg" alt="image1">
                    <img class = "grid_item" src="../../static/imgs/3-2.jpg" alt="image2">
                    <img class = "grid_item" src="../../static/imgs/3-3.jpg" alt="image3">
                    <img class = "grid_item" src="../../static/imgs/3-4.jpg" alt="image4">
                    <img class = "grid_item" src="../../static/imgs/3-1.jpg" alt="image5">
                    <img class = "grid_item" src="../../static/imgs/3-2.jpg" alt="image6">
                    <img class = "grid_item" src="../../static/imgs/3-3.jpg" alt="image7">
                    <img class = "grid_item" src="../../static/imgs/3-4.jpg" alt="image8">
                </div>
            </div>
        </div>

        <!-- 네번째 페이지  -->
        <div id="Contact" class="listItem">
            <h1> Contact </h1>
            <iframe width="560" height="315" src="https://www.youtube.com/embed/0xJxgvJO2Xo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

            <div class="ContactLinkWrapper">
                <a href="ehttps://velog.io/" class="ContactLink">Blog</a>
                <a href="mailtotest@gmail.com/" class="ContactLink">Gmail</a>
                <a href="https://github.com/" class="ContactLink">Github</a>
            </div>
        </div>
        <footer>
            This site is a learning page through Django.
        </footer>
    <div>
</body>
</html>
```

### CSS

```css
body{
    margin: 0;

    font-family: 'Poiret One',cursive;
    line-height: 40px;
    color: white;
    text-align: center;
}

.listItem{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    width: 100%;
    height: 100vh;

    scroll-snap-align: center;
}

.listItem:nth-child(2){
    background-color: #DAB88B;
}

.listItem:nth-child(3){
    background-color: #BFB5D7;
}

.listItem:nth-child(4){
    background-color: #FEDCCC;
}

.listItem:nth-child(5){
    background-color: #B7CADB;
}

nav{
    display: flex;
    justify-content: center;
    align-items: center;

    width: 100%;
    height: 100px;

    text-align: center;
    font-size: 20px;
    font-style: italic;

    position: fixed;
    background-color: rgba(200, 240, 240, 0.9);
}

nav li{
    margin: 60px;
    display: inline;
}

nav a{
    color: black;
}

#container{
    width: 100%;
    height: 100vh;
    overflow: auto;

    scroll-behavior: smooth;
    scroll-snap-type: y mandatory;
}

.profile {
    padding: 0.5rem;

    border-radius: 30%;
    margin-top: 20px;
    background-color: rgba(255,255,255,0.1);
    border: 1px solid rgba(255,255,255,0.5);
}

.profile img{
    border-radius: 30%;
}
.AboutContents{
    float: right;
    margin-left: 100px;
}

.GalleryItems{
    display: grid;

    grid-template-columns: repeat(4,1fr);
    grid-template-rows: repeat(2,200px);
    gap:50px;
}

.grid_item{
    border-radius: 45px;
    width: 200px;
    height: 200px;
}

.Contact{
    text-align: center;
}

.ContactLink{
    margin: 45px;
    color: white;
    font-size: 40px;
    font-style: italic;
    text-decoration: none;
}


footer{
    background-color: black;
}
```