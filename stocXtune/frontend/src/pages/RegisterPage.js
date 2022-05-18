import { useState } from "react";
import { backendBaseUrl } from "../core/constants";
import useFetch from "../services/useFetch"
import {useFormik} from 'formik'
import * as Yup from 'yup';
import {LoadingIndicator} from "../components/LoadingIndicator";
import {trackPromise} from "react-promise-tracker";
import {BackendService} from "../services/backendService";

export default function RegisterPage() {
    // States for checking errors
    const [isSubmitting, setIsSubmitting] = useState(true)
    const [error, setError] = useState(false)

    const validate = values => {
        const errors = {}

        // firstName
        if (!values.firstName)
            errors.firstName = 'Required'
        else if (values.firstName < 2)
            errors.firstName = 'First name is too short'

        // lastName
        if (!values.lastName)
            errors.lastName = 'Required'
        else if (values.lastName < 2)
            errors.lastName = 'Last name is too short'


        // email
        if (!values.email) {
            errors.email = 'Required';
        } else if (!/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i.test(values.email)) {
            errors.email = 'Invalid email address';
        }

        // password
        if (!values.password) {
            errors.password = 'Required'
        }
        else if (values.password < 3) {
            errors.password = 'Password is too short'
        }


        // confirm password
        if (values.password !== values.confirmPassword)
            errors.confirmPassword = 'Password does not match'

        return errors

    }

    const form = useFormik({
        initialValues: {
            firstName: '',
            lastName: '',
            userName: '',
            email: '',
            password: '',
            confirmPassword: ''
        },
        validate,
        validationSchema: Yup.object({
            firstName: Yup.string()
                .min(2, 'Must be 2 characters or more')
                .required('Required'),
            lastName: Yup.string()
                .min(2, 'Must be 2 characters or more')
                .required('Required'),
            email: Yup.string().email('Invalid email address')
                .required('Required'),
            password: Yup.string().required('Required'),
            confirmPassword:  Yup.string().required('Required'),

        }),
        onSubmit: async (values,{setSubmitting}) => {
            setSubmitting(true)


            trackPromise(BackendService.register({
                first_name: values.firstName,
                last_name: values.lastName,
                user_name: values.email,
                email: values.email,
                password: values.password
            })
                .then(success => {
                    console.log('Registration successful', success)
                })
                .catch(e => {
                    console.error('Registration failed', e)
                })
                .finally(() => {
                    console.log('Submission completed')
                    setSubmitting(false);
                })
            )

            // setTimeout(() => {
            //     const [data, error, loading] = useFetch(backendBaseUrl,null,'/user/register','POST',{
            //         ...values
            //     },)
            //     setSubmitting(false);
            //     setIsSubmitting(isSubmitting);
            // }, 2000);
        }
    })



    console.log('is submitting',form.isSubmitting)
    if (form.isSubmitting) {
        return <progress className="progress w-56"/>
    }
    return (

        <section className="pt-32 bg-cover bg-[url('../public/assets/register_bg.png')] min-h-screen">
            <div className='space-y-20 pb-16 container mx-auto grid grid-4'>
                <form onSubmit={form.handleSubmit} className='pt-8 col-span-4 lg:col-span-1 max-w-screen-sm  px-4 lg:px-8 space-y-8'>
                   <div className="space-y-6">
                       <div className="uppercase text-2xl font-light">Start for Free</div>
                       <div className='text-3xl lg:text-4xl font-bold '>Create a new Account</div>
                       <div className="text-xl">Already a Member? <a className="text-lighter-teal" href="/">Login</a></div>
                   </div>

                    <div className="alert alert-success shadow-lg">
                        <div>
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                                 className="stroke-current flex-shrink-0 w-6 h-6">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                      d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                            </svg>
                            <span>Your registration is successful! Login to continue</span>
                        </div>
                        <div className="flex-none">
                            <button className="btn btn-primary btn-sm">Login</button>
                        </div>
                    </div>

                    <div className="grid grid-cols-2 gap-8">
                       <div>
                           <label htmlFor="firstName">First Name</label>
                           <input name="firstName" id="firstName" type="text" value={form.values.firstName} onChange={form.handleChange}
                                  onBlur={form.handleBlur}
                               className='`mr-2 h-14 text-md bg-lighter-teal/20 input w-full placeholder:capitalize placeholder:text-neutral/50`'
                               placeholder='First Name'  aria-autocomplete="list"/>
                               {form.touched.firstName && form.errors.firstName ? <div className="text-error">{form.errors.firstName}</div> : null}
                       </div>
                        <div>
                            <label htmlFor="lastName">Last Name</label>
                            <input name="lastName" id="lastName" type="text" value={form.values.lastName} onChange={form.handleChange}
                                   onBlur={form.handleBlur}
                                className=' mr-2 h-14  text-md bg-lighter-teal/20 input w-full placeholder:capitalize placeholder:text-neutral/50'
                                placeholder='Last Name'  aria-autocomplete="list"/>
                            {form.touched.lastName && form.errors.lastName ? <div className="text-error">{form.errors.lastName}</div> : null}
                        </div>
                        <div className="col-span-2">
                            <label htmlFor="email">Email Address</label>
                            <input name="email" id="email" type="email" value={form.values.email} onChange={form.handleChange}
                                   onBlur={form.handleBlur}
                                className=' mr-2 h-14  text-md bg-lighter-teal/20 input w-full placeholder:capitalize placeholder:text-neutral/50'
                                placeholder='Email Address'  aria-autocomplete="list"/>
                            {form.touched.email && form.errors.email ? <div className="text-error">{form.errors.email}</div> : null}
                        </div>
                        <div className="col-span-2">
                            <label htmlFor="password">Password</label>
                            <input name="password" id="password" type="password" value={form.values.password} onChange={form.handleChange}
                                   onBlur={form.handleBlur}
                                className=' mr-2 h-14 text-md bg-lighter-teal/20 input w-full placeholder:capitalize placeholder:text-neutral/50'
                                placeholder='Enter password'  aria-autocomplete="list"/>
                            {form.touched.password && form.errors.password ? <div className="text-error">{form.errors.password}</div> : null}
                        </div>
                        <div className="col-span-2">
                            <label htmlFor="confirmPassword">Re-enter Password</label>
                            <input name="confirmPassword" id="confirmPassword" type="password" value={form.values.confirmPassword} onChange={form.handleChange}
                                   onBlur={form.handleBlur}
                                className=' mr-2 h-14  text-md bg-lighter-teal/20 input w-full placeholder:capitalize placeholder:text-neutral/50'
                                placeholder='Confirm your password'  aria-autocomplete="list"/>
                            {form.touched.confirmPassword && form.errors.confirmPassword ? <div className="text-error">{form.errors.confirmPassword}</div> : null}
                        </div>
                        <button type="submit" disabled={form.dirty && !form.isValid} className="btn btn-primary col-span-2 btn-lg" >Create an Account {form.isSubmitting} {form.isSubmitting ? <div>Submitting</div>:null}</button>
                        {<LoadingIndicator/>}
                    </div>
                </form>
                <div className="col-span-3">

                </div>

            </div>
        </section>
    )
}
