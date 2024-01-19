export class ResponseDto<T> {
  constructor(
    public ok: boolean,
    public status: number,
    public data: T = null,
  ) {}
}
