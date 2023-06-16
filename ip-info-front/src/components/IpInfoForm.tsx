import React, { useState, useEffect } from 'react';
import { useForm, SubmitHandler } from "react-hook-form";

import './IpInfoForm.css';

type Inputs = {
  ip: string,
  exampleRequired: string,
};

type ipInfo = {
  ip: string
  type: any
  continent_code: string
  continent_name: string
  country_code: string
  country_name: string
  region_code: string
  region_name: string
  city: string
  zip: string
  latitude: number
  longitude: number
  location: any
  country_flag: string
  country_flag_emoji: string
  country_flag_emoji_unicode: string
  calling_code: string
  is_eu: boolean
}

export default function IpInfoForm() {
  const [ipInfo, setIpInfo] = useState('');
  const { register, handleSubmit, formState: { errors } } = useForm<Inputs>();
  const onSubmit: SubmitHandler<Inputs> = (data) => sendIpData(data);

  const sendIpData = (data: any) => {
    const requestOptions = {
      method: 'GET',
      headers: { 'Content-Type': 'application/json' },
    };
    
    fetch('/api/v1/ipinfo/' + data.ip, requestOptions)
        .then(response => response.json())
        .then(data => {
          setIpInfo(data)
          console.log(data);
        });
  }

  return (
    <div>
      <form onSubmit={handleSubmit(onSubmit)} className="ip-info-form">
        <input defaultValue="46.191.249.55" {...register("ip")} />
        {errors.exampleRequired && <span>This field is required</span>}
        
        <input type="submit" />
      </form>

      <textarea
        defaultValue={ipInfo}
        readOnly
      >
      </textarea>
    </div>
  );
}
