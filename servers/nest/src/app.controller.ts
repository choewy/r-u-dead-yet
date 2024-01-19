import { Body, Controller, Get, Post } from '@nestjs/common';

import { ResponseDto } from './common';

@Controller()
export class AppController {
  @Get()
  get() {
    return new ResponseDto(true, 200, 'home');
  }

  @Post()
  post(@Body() body: any) {
    return new ResponseDto(true, 201, body);
  }
}
