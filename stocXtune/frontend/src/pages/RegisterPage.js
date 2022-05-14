import { useState } from "react";
import { backendBaseUrl } from "../core/constants";
import useFetch from "../services/useFetch"

export default function RegisterPage() {
    // States for trackin user registration form fields
    const [firstName, setFirstName] =useState('')
    const [lastName, setLastName] =useState('')
    const [userName, setUserName] =useState('')
    const [email, setEmail] =useState('')
    const [password, setPassword] =useState('')
    const [confirmPassword, setConfirmPassword] =useState('')

    

    // States for checking errors
    const [submitted, setSubmitted] = useState(false)
    const [error, setError] = useState(false)

    

    // Handle on FirstNName change event
    const handleInput = (event) => {
        console.log(event.target.id)
       
        

        switch (event.target.id) {
            case 'firstName':
                console.log('setting firstName')
                setFirstName(event.target.value)
                break;
            case 'lastName':
                console.log('setting lastname')
                setLastName(event.target.value)
                break;

            case 'email':
                console.log('setting email')
                setEmail(event.target.value)
                break;

            case 'password':
                console.log('setting password')
                setPassword(event.target.value)
                break;
            case 'confirmPassword':
                console.log('setting confirm password')
                setConfirmPassword(event.target.value)
                break;
            default:
                break;
        }
        setSubmitted(false);
    }

    return (
        <section className="pt-32 bg-cover bg-[url('../public/assets/register_bg.png')] min-h-screen">
            <div className='space-y-20 pb-16 container mx-auto grid grid-4'>
                <div className='pt-8 col-span-4 lg:col-span-1 max-w-screen-sm  px-4 lg:px-8 space-y-8'>
                   <div className="space-y-6">
                       <div className="uppercase text-2xl font-light">Start for Free</div>
                       <div className='text-3xl lg:text-4xl font-bold '>Create a new Account</div>
                       <div className="text-xl">Already a Member? <a className="text-lighter-teal" href="/">Login</a></div>
                   </div>

                    <div className="grid grid-cols-2 gap-8">
                       <div>
                           <label>First Name</label>
                           <input name="firstName" id="firstName" value={firstName} onChange={handleInput}
                               className=' mr-2 h-14 uppercase text-md bg-lighter-teal/20 input w-full placeholder:capitalize placeholder:text-neutral/50'
                               placeholder='First Name' type="text" aria-autocomplete="list"/>
                       </div>
                        <div>
                            <label>Last Name</label>
                            <input name="lastName" id="lastName" value={lastName} onChange={handleInput}
                                className=' mr-2 h-14 uppercase text-md bg-lighter-teal/20 input w-full placeholder:capitalize placeholder:text-neutral/50'
                                placeholder='Last Name' type="text" aria-autocomplete="list"/>
                        </div>
                        <div className="col-span-2">
                            <label>Email Address</label>
                            <input name="email" id="email" value={email} onChange={handleInput}
                                className=' mr-2 h-14 uppercase text-md bg-lighter-teal/20 input w-full placeholder:capitalize placeholder:text-neutral/50'
                                placeholder='Email Address' type="email" aria-autocomplete="list"/>
                        </div>
                        <div className="col-span-2">
                            <label>Password</label>
                            <input name="password" id="password" value={password} onChange={handleInput}
                                className=' mr-2 h-14 uppercase text-md bg-lighter-teal/20 input w-full placeholder:capitalize placeholder:text-neutral/50'
                                placeholder='Enter password' type="password" aria-autocomplete="list"/>
                        </div>
                        <div className="col-span-2">
                            <label>Re-enter Password</label>
                            <input name="confirmPassword" id="confirmPassword" value={confirmPassword} onChange={handleInput}
                                className=' mr-2 h-14 uppercase text-md bg-lighter-teal/20 input w-full placeholder:capitalize placeholder:text-neutral/50'
                                placeholder='Confirm your password' type="password" aria-autocomplete="list"/>
                        </div>
                        <button  className="btn btn-primary col-span-2 btn-lg">Create an Account</button>
                    </div>
                </div>
                <div className="col-span-3"></div>

            </div>
        </section>
    )
}
