import com.codeborne.selenide.Configuration;
import org.junit.jupiter.api.Test;

import static com.codeborne.selenide.Condition.text;
import static com.codeborne.selenide.Selenide.$;
import static com.codeborne.selenide.Selenide.open;


public class LoginTests {

    @Test
    void successfullLoginTest() {
        Configuration.holdBrowserOpen = true; // чтобы браузер не закрывался

        // открыть форму авторизации
        open("https://school.qa.guru/cms/system/login");

        // ввести адрес электронной почты
        $("[name=email]").setValue("hello@qa.guru");

        // ввести пароль
        $("[name=password]").setValue("qagurupassword");

        // нажать кнопку "Войти"
        $("[class=btn-success]").click();

        // нажать на кнопку "Личный кабинет"
        $(".main-heder__login").click();

        // проверить успешную авторизацию
        $(".logined-form").shouldHave(text("QA_GURU_BOT"));
    }
}
