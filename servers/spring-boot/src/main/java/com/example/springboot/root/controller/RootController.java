package com.example.springboot.root.controller;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.springboot.common.dto.ResponseDto;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;


@RestController
@RequestMapping("/")
public class RootController {
  private final Logger logger = LoggerFactory.getLogger(this.getClass().getSimpleName());

  @GetMapping
  public ResponseDto<String> home() {
    ResponseDto<String> dto= new ResponseDto<>();

    dto.setStatus(200);
    dto.setData("home");

    return dto;
  }

  @PostMapping
  public ResponseDto<String> post(@RequestBody String packet) {
    this.logger.info(packet);

    ResponseDto<String> dto= new ResponseDto<>();

    dto.setStatus(201);
    dto.setData(packet);

    return dto;
  }
}
