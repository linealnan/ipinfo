import { useForm, SubmitHandler } from "react-hook-form";

import './IpInfoForm.css';

type Inputs = {
  example: string,
  exampleRequired: string,
};

export default function IpInfoForm() {
  const { register, handleSubmit, watch, formState: { errors } } = useForm<Inputs>();
  const onSubmit: SubmitHandler<Inputs> = data => console.log(data);

  console.log(watch("example")) // watch input value by passing the name of it

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="ip-info-form">
      <input defaultValue="test" {...register("example")} />
      {errors.exampleRequired && <span>This field is required</span>}
      
      <input type="submit" />
    </form>
  );
}
