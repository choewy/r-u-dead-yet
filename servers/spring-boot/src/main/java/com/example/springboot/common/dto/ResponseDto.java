package com.example.springboot.common.dto;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class ResponseDto<T> {
  private Integer status;
  private T data;
}
