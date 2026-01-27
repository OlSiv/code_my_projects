package com.demo;

import org.junit.jupiter.api.Test;

import java.time.DayOfWeek;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class FirstTest {

    @Test
    void shouldOpen() {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd.MM.yyyy");
        LocalDate localDate = LocalDate.parse("28.10.2025", formatter);
        assertEquals(DayOfWeek.TUESDAY, localDate.getDayOfWeek());
    }
}
